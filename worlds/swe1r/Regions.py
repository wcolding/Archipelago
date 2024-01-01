from BaseClasses import MultiWorld, Region, Entrance, Location
from .Locations import *
from .Rules import *
from ..generic.Rules import set_rule
import typing

location_name_to_id = dict

def create_swe1r_regions(world: MultiWorld, player: int, base_id: int):
    location_name_to_id = get_offset_location_table(base_id)

    menu_region = Region("Menu", player, world)
    world.regions.append(menu_region)

    # May break this up into race-completion chunks
    watto_shop_region = Region("Watto's Shop", player, world)
    for check in wattos_shop_table:
        watto_shop_region.locations += [SWRacerLocation(player, check, location_name_to_id[check], watto_shop_region)]
    world.regions.append(watto_shop_region)

    # Circuits
    amateur_circuit_region = create_region_with_rule(world, player, "Amateur Circuit", course_clears_amateur_table, lambda state: True)
    world.regions.append(amateur_circuit_region)

    semipro_circuit_region = create_region_with_rule(world, player, "Semi-Pro Circuit", course_clears_semipro_table, lambda state: semipro_unlocked(world, player))
    world.regions.append(semipro_circuit_region)

    galactic_circuit_region = create_region_with_rule(world, player, "Galactic Circuit", course_clears_galactic_table, lambda state: galactic_unlocked(world, player))
    world.regions.append(galactic_circuit_region)

    invitational_circuit_region = create_region_with_rule(world, player, "Invitational Circuit", course_clears_invitational_table, lambda state: invitational_unlocked(world, player))
    world.regions.append(invitational_circuit_region)

    # Conditionally-available locations
    if pit_shop_available(world, player):
        pit_droid_shop_region = create_region_with_rule(world, player, "Pit Droid Shop", pit_droid_shop_table, lambda state: True)
        world.regions.append(pit_droid_shop_region)
        menu_region.connect(pit_droid_shop_region) 
    
    # Connect regions
    menu_region.connect(watto_shop_region)
    menu_region.connect(amateur_circuit_region)
    menu_region.connect(semipro_circuit_region)
    menu_region.connect(galactic_circuit_region)
    menu_region.connect(invitational_circuit_region)

def create_region_with_rule(world: MultiWorld, player: int, name: str, location_names: dict, rule: typing.Callable[[], bool]):
    new_reg = Region(name, player, world)
    for loc in location_names:
        new_loc = SWRacerLocation(player, loc, location_name_to_id[loc], new_reg)
        set_rule(new_loc, rule)
        new_reg.locations.append(new_loc)
    return new_reg