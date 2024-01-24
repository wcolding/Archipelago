from typing import Any, Dict
import random

from BaseClasses import Item
from ..AutoWorld import World
from .Options import *
from .Items import *
from .Locations import *
from .Regions import *

class SWRWorld(World):
    """
    Star Wars Episode I: Racer is a racing game where the player wins prize money and buys upgrades for their vehicle.
    This randomizer shuffles race rewards as well as shop items. It also randomizes track order and available racers.
    Now THIS is podracing!
    """
    game: str = "Star Wars Episode I Racer"
    topology_present = False
    options_dataclass = SWROptions
    options: SWROptions

    required_client_version = (0, 4, 4)

    item_name_to_id = get_item_name_to_id()
    location_name_to_id = get_location_name_to_id()

    racers_pool = racers_table
    starting_racers_flag = 0
    randomized_courses = dict()
    randomized_course_names = list()

    def set_starting_racers(self):
        if self.multiworld.starting_racers[self.player].value == 0:
            # Vanilla
            for racer in vanilla_racers_list:
                self.starting_racers_flag |= self.racers_pool.pop(racer).bitflag
        else:
            # Random Range
            rand_range = self.multiworld.number_of_starting_racers[self.player].value
            racer_names = list(racers_table.keys())
            random.shuffle(racer_names)
            
            for i in range(0, rand_range):
                selected_racer = racer_names.pop()
                self.starting_racers_flag |= self.racers_pool.pop(selected_racer).bitflag        

    def randomize_courses(self):
        course_clears = list(course_clears_table.keys())
        course_names = list(courses_table.keys())
        self.randomized_course_names = list(course_names)
        random.shuffle(self.randomized_course_names)

        for i in range(0, len(self.randomized_course_names)):
            self.randomized_courses[i] = courses_table[self.randomized_course_names[i]]
            self.multiworld.spoiler.set_entrance(f"{course_clears[i]} ({course_names[i]})", self.randomized_course_names[i], 'entrance', self.player)

    def generate_early(self):
        self.set_starting_racers()
        self.randomize_courses()

        # Option shortcuts
        self.progressive_parts = self.multiworld.progressive_parts[self.player].value
        self.progressive_circuits = self.multiworld.progressive_circuits[self.player].value
        self.invitational_pass = self.multiworld.invitational_circuit_pass[self.player].value
        self.allow_pit_droids = not self.multiworld.disable_part_degradation[self.player].value

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "StartingRacers": self.starting_racers_flag,
            "Courses": self.randomized_courses,
            "ProgressiveParts": self.multiworld.progressive_parts[self.player].value,
            "ProgressiveCircuits": self.multiworld.progressive_circuits[self.player].value,
            "EnableInvitationalCircuitPass": self.multiworld.invitational_circuit_pass[self.player].value,
            "DisablePartDegradation": self.multiworld.disable_part_degradation[self.player].value,
            "DeathLink": self.multiworld.deathlink[self.player].value
        }
    
    def create_regions(self) -> None:
        return create_swr_regions(self)

    def create_item(self, name: str) -> Item:
        item_data = full_item_table[name]
        return SWRItem(name, item_data.classification, item_data.id, self.player)
    
    def append_items_from_data(self, name: str, count_override: int | None = None):
        item_data = full_item_table[name]
        count = item_data.max_allowed
        if count_override != None:
            count = count_override

        self.multiworld.itempool += [SWRItem(name, item_data.classification, item_data.id, self.player) for i in range(0, count)]

    def create_items(self) -> None:
        # Pod Parts
        if self.progressive_parts:
            for part in pod_progressive_upgrades_table:
                self.append_items_from_data(part)
        else:
            for part in pod_upgrades_table:
                self.append_items_from_data(part)

        # Pit Droids
        if self.allow_pit_droids:
            self.append_items_from_data("Pit Droid")

        # Circuits
        if self.progressive_circuits:
            if self.invitational_pass:
                self.append_items_from_data("Progressive Circuit Pass")
            else:
                self.append_items_from_data("Progressive Circuit Pass", 2)
        else:
            self.append_items_from_data("Semi-Pro Circuit Pass")
            self.append_items_from_data("Galactic Circuit Pass")
            if self.invitational_pass:
                self.append_items_from_data("Invitational Circuit Pass")
        
        # Racers
        for racer in self.racers_pool:
            self.append_items_from_data(racer)

        # Money
        for item in money_item_table:
            self.append_items_from_data(item)

    def set_rules(self) -> None:
        return super().set_rules()