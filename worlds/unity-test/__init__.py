from ..AutoWorld import World
from .Items import UTItem, item_table
from .Locations import location_table
from .Options import UT_options
from .Rules import set_rules
from .Regions import create_regions
from BaseClasses import Region, RegionType, Entrance, Item, MultiWorld

class UTWorld(World):
    """
    This game is entirely made up
    """

    game: str = "Unity Test"
    topology_present = False
    item_name_to_id = item_table
    location_name_to_id = location_table
    options = UT_options
    remote_items: bool = False

    data_version = 5
    forced_auto_forfeit = False

#def generate_early(self):
    #

    def create_regions(self):
        create_regions(self.world, self.player)

    def create_item(self, name: str) -> UTItem:
        return UTItem(name, name.find('Rupee') == -1, item_table[name], self.player)

    def create_items(self):
        self.world.itempool += [self.create_item("Hero's Sword")]
        self.world.itempool += [self.create_item("Hero's Shield")]
        self.world.itempool += [self.create_item("Mega Hammer")]
        self.world.itempool += [self.create_item("Hookshot")]
        self.world.itempool += [self.create_item("Bombs")]
        self.world.itempool += [self.create_item("Hero's Bow")]
        
        self.world.itempool += [self.create_item("Green Rupee")]
        self.world.itempool += [self.create_item("Blue Rupee") for i in range(0,10)]
        self.world.itempool += [self.create_item("Red Rupee") for i in range(0,3)]
        self.world.itempool += [self.create_item("Purple Rupee") for i in range(0,2)]
        self.world.itempool += [self.create_item("Silver Rupee") for i in range(0,2)]
        self.world.itempool += [self.create_item("Gold Rupee")]

    def set_rules(self):
        set_rules(self.world, self.player)

    #def generate_basic(self):
        #self.create_items()