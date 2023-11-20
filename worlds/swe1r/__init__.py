from ..AutoWorld import World
from .Items import *
from .Locations import *
from .Options import *
import random

from BaseClasses import Region, ItemClassification

class SWRWorld(World):
    """
    Now THIS is podracing!
    """

    game: str = "Star Wars Episode I Racer"
    topology_present = False
    option_definitions = swr_options

    base_id = 11380000

    item_name_to_id = get_offset_item_table(base_id)
    location_name_to_id = get_offset_location_table(base_id)

    data_version = 9
    required_client_version = (0, 4, 2)

    starting_racers_list = [] 
    racers_flag = 0
    randomized_courses_list = []

    def set_starting_racers(self):
        match (self.multiworld.starting_racers[self.player].value):
            case 0: # Vanilla
                self.starting_racers_list = vanilla_racers_list
            case 1: # Random One
                single_selection = random.randint(0, len(racers_table) - 1)
                index = 0
                for racer,id in racers_table.items():
                    if index == single_selection:
                        self.starting_racers_list = [racer]
                    index += 1
            case 2: # Random Range
                rand_range = self.multiworld.number_of_starting_racers[self.player].value

                remaining_racers = list(racers_table.keys())
                # for racer,id in racers_table.items():
                #     remaining_racers += [racer]
                
                for i in range(0, rand_range):
                    selection = remaining_racers[random.randint(0, len(remaining_racers) - 1)]
                    remaining_racers.remove(selection)
                    self.starting_racers_list += [selection]
            case _:
                pass

        for racer in self.starting_racers_list:
            self.racers_flag |= racers_table[racer][1]

    def randomize_courses(self):
        courses_list = list(courses_table.keys())
        remaining_courses = list(courses_list)
        course_locations_list = list(course_clears_table.keys())

        for i in range(0, len(courses_table)):
            selection = remaining_courses[random.randint(0, len(remaining_courses) - 1)]
            remaining_courses.remove(selection)
            self.randomized_courses_list += [courses_table[selection]]
            self.multiworld.spoiler.set_entrance("{location} ({old})".format(location = course_locations_list[i], old = courses_list[i]), selection, 'entrance', self.player)

    def generate_early(self):
        self.set_starting_racers()
        self.randomize_courses()

    def fill_slot_data(self):
        return {
            "StartingRacers": self.racers_flag,
            "Courses": self.randomized_courses_list,
            "ProgressiveParts": self.multiworld.progressive_parts[self.player].value,
            "ProgressiveCircuits": self.multiworld.progressive_circuits[self.player].value,
            "InvitationalCircuitBehavior": self.multiworld.invitational_circuit_behavior[self.player].value,
            "DisablePartDegradation": self.multiworld.disable_part_degradation[self.player].value,
            "RequiredPlacement": self.multiworld.required_placement[self.player].value
        }

    def create_regions(self):
        region_menu = Region("Menu", self.player, self.multiworld)
        for loc in location_table:
            region_menu.locations.append(SWRacerLocation(self.player, loc, self.location_name_to_id[loc], region_menu))
        self.multiworld.regions.append(region_menu)

    def create_item(self, name: str) -> "Item":
        id = self.item_name_to_id[name]
        if "Circuit Pass" in name:
            item_type = ItemClassification.progression
        else:
            item_type = ItemClassification.filler
        return SWRacerItem(name, item_type, id, self.player)

    def create_items(self):
        if (self.multiworld.progressive_parts[self.player].value):
            for part in pod_progressive_item_table:
                self.multiworld.itempool += [self.create_item(part) for i in range(0,5)]
        else:
            for part in pod_item_table:
                self.multiworld.itempool += [self.create_item(part)]

        if not (self.multiworld.disable_part_degradation[self.player].value):
            self.multiworld.itempool += [self.create_item("Pit Droid") for i in range(0,3)]

        if (self.multiworld.progressive_circuits[self.player].value):
            passes_count = 2
            if (self.multiworld.invitational_circuit_behavior[self.player].value == 1):
                passes_count += 1
            self.multiworld.itempool += [self.create_item("Progressive Circuit Pass") for i in range(0, passes_count)]
        else:
            self.multiworld.itempool += [self.create_item("Semi Pro Circuit Pass")]
            self.multiworld.itempool += [self.create_item("Galactic Circuit Pass")]
            if (self.multiworld.invitational_circuit_behavior[self.player].value == 1):
                self.multiworld.itempool += [self.create_item("Invitational Circuit Pass")]

        for racer in racers_table:
            if racer not in self.starting_racers_list:
                self.multiworld.itempool += [self.create_item(racer)]

    def set_rules(self) -> None:
        return super().set_rules()