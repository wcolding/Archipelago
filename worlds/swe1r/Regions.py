from BaseClasses import MultiWorld, Region, CollectionState, Entrance, Location

from .Options import ProgressiveCircuits, InvitationalCircuitBehavior
from .Locations import *
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

    # Circuits
    amateur_locations = get_locations("amateur")
    semipro_locations = get_locations("semipro")
    galactic_locations = get_locations("galactic")
    invitational_locations = get_locations("invitational")

    amateur_circuit_region = create_region_with_rule(world, player, "Amateur Circuit", amateur_locations, lambda state: True)
    
    if (world.progressive_circuits[player].value):
        semipro_circuit_region = create_region_with_rule(world, player, "Semi-Pro Circuit", semipro_locations, lambda state: state.has("Progressive Circuit Pass", player, 1))
        galactic_circuit_region = create_region_with_rule(world, player, "Galactic Circuit", galactic_locations, lambda state: state.has("Progressive Circuit Pass", player, 2))
    else:
        semipro_circuit_region = create_region_with_rule(world, player, "Semi-Pro Circuit", semipro_locations, lambda state: state.has("Semi Pro Circuit Pass", player))
        galactic_circuit_region = create_region_with_rule(world, player, "Galactic Circuit", galactic_locations, lambda state: state.has("Galactic Circuit Pass", player))

    if (world.invitational_circuit_behavior[player].value == InvitationalCircuitBehavior.option_vanilla):
        # Player needs 1st place in all tracks in each preceding circuit to unlock the first three tracks in the invitation
        # For now we will treat it as all or nothing
        invitational_circuit_region = create_region_with_rule(world, player, "Invitational Circuit", invitational_locations, lambda state: state.can_reach("Semi-Pro Circuit", 'Region', player) and state.can_reach("Galactic Circuit", 'Region', player))
    else:
        if (world.progressive_circuits[player].value):
            invitational_circuit_region = create_region_with_rule(world, player, "Invitational Circuit", invitational_locations, lambda state: state.has("Progressive Circuit Pass", player, 3))
        else:
            invitational_circuit_region = create_region_with_rule(world, player, "Invitational Circuit", invitational_locations, lambda state: state.has("Invitational Circuit Pass", player))
    
    world.regions.append(amateur_circuit_region)
    world.regions.append(semipro_circuit_region)
    world.regions.append(galactic_circuit_region)
    world.regions.append(invitational_circuit_region)

    # Conditionally-available locations
    if not world.disable_part_degradation[player].value:
        pit_droid_shop_region = create_region_with_rule(world, player, "Pit Droid Shop", pit_droid_shop_table.keys(), lambda state: True)
        world.regions.append(pit_droid_shop_region)
        menu_region.connect(pit_droid_shop_region) 
    
    # Connect regions
    menu_region.connect(watto_shop_region)
    menu_region.connect(amateur_circuit_region)
    menu_region.connect(semipro_circuit_region)
    menu_region.connect(galactic_circuit_region)
    menu_region.connect(invitational_circuit_region)

    # All courses available
    world.completion_condition[player] = lambda state: state.can_reach("Semi-Pro Circuit", 'Region', player) and state.can_reach("Galactic Circuit", 'Region', player) and state.can_reach("Invitational Circuit", 'Region', player)

def create_region_with_rule(world: MultiWorld, player: int, name: str, location_names: list, rule: typing.Callable[[CollectionState], bool]) -> Region:
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