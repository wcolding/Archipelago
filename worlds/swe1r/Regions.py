from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import *
from .Rules import *
from ..generic.Rules import set_rule
import typing

location_name_to_id = {}
course_id_to_name = {}
randomized_courses = {}

circuit_data = {
    "amateur": [course_clears_amateur_table, 0, 7],
    "semipro": [course_clears_semipro_table, 7, 14],
    "galactic": [course_clears_galactic_table, 14, 21],
    "invitational": [course_clears_invitational_table, 21, 25],
}

def create_swe1r_regions(world: MultiWorld, player: int, base_id: int, _randomized_courses: dict):
    global location_name_to_id 
    global course_id_to_name
    global randomized_courses
    location_name_to_id = get_offset_location_table(base_id)
    course_id_to_name = {val: key for key, val in courses_table.items()}
    randomized_courses = _randomized_courses

    menu_region = Region("Menu", player, world)
    world.regions.append(menu_region)

    # May break this up into race-completion chunks
    watto_shop_region = Region("Watto's Shop", player, world)
    for check in wattos_shop_table:
        watto_shop_region.locations += [SWRacerLocation(player, check, location_name_to_id[check], watto_shop_region)]
    world.regions.append(watto_shop_region)

    # # Circuits
    amateur_locations = get_locations("amateur")
    amateur_circuit_region = create_region_with_rule(world, player, "Amateur Circuit", amateur_locations, lambda state: True)
    world.regions.append(amateur_circuit_region)

    semipro_locations = get_locations("semipro")
    semipro_circuit_region = create_region_with_rule(world, player, "Semi-Pro Circuit", semipro_locations, lambda state: semipro_unlocked(world, player))
    world.regions.append(semipro_circuit_region)

    galactic_locations = get_locations("galactic")
    galactic_circuit_region = create_region_with_rule(world, player, "Galactic Circuit", galactic_locations, lambda state: galactic_unlocked(world, player))
    world.regions.append(galactic_circuit_region)
    
    invitational_locations = get_locations("invitational")
    invitational_circuit_region = create_region_with_rule(world, player, "Invitational Circuit", invitational_locations, lambda state: invitational_unlocked(world, player))
    world.regions.append(invitational_circuit_region)

    # Conditionally-available locations
    if pit_shop_available(world, player):
        pit_droid_shop_region = create_region_with_rule(world, player, "Pit Droid Shop", pit_droid_shop_table.keys(), lambda state: True)
        world.regions.append(pit_droid_shop_region)
        menu_region.connect(pit_droid_shop_region) 
    
    # Connect regions
    menu_region.connect(watto_shop_region)
    menu_region.connect(amateur_circuit_region)
    menu_region.connect(semipro_circuit_region)
    menu_region.connect(galactic_circuit_region)
    menu_region.connect(invitational_circuit_region)

def create_region_with_rule(world: MultiWorld, player: int, name: str, location_names: list, rule: typing.Callable[[], bool]) -> Region:
    new_reg = Region(name, player, world)
    for loc in location_names:
        new_loc = SWRacerLocation(player, loc, location_name_to_id[loc], new_reg)
        set_rule(new_loc, rule)
        new_reg.locations.append(new_loc)
    return new_reg

def get_randomized_course_names(randomized_courses: dict, start: int, end: int) -> list:
    names = []
    names += [course_id_to_name[randomized_courses[i]] for i in range(start,end)]
    return names

def get_matching_racer_unlocks(circuit_courses: list) -> list:
    unlocks = []
    for loc in racer_unlocks_table.keys():
        if loc.removeprefix("Racer Unlock - ") in circuit_courses:
            unlocks += [loc]
    return unlocks

def get_locations(circuit_name: str) -> list:
    courses = get_randomized_course_names(randomized_courses, circuit_data[circuit_name][1], circuit_data[circuit_name][2])
    locations = list(circuit_data[circuit_name][0].keys()) + get_matching_racer_unlocks(courses)
    return locations