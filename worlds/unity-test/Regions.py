from BaseClasses import MultiWorld, Region, Entrance, Location, RegionType
from .Locations import UTLocation, location_table

def create_regions(world: MultiWorld, player: int):
    mainReg = Region("Menu", RegionType.Generic, "Menu", player, world)
    for loc in location_table:
        mainReg.locations.append(UTLocation(player, loc, location_table[loc], mainReg))
    world.regions.append(mainReg)