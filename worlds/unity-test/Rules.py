from ..generic.Rules import set_rule

def set_rules(world,player):
    set_rule(world.get_location("Box 0", player), lambda state: True)
    set_rule(world.get_location("Box 1", player), lambda state: True)
    set_rule(world.get_location("Box 2", player), lambda state: True)
    set_rule(world.get_location("Box 3", player), lambda state: True)
    set_rule(world.get_location("Box 4", player), lambda state: True)
    
    set_rule(world.get_location("Box 5", player), lambda state: True)
    set_rule(world.get_location("Box 6", player), lambda state: True)
    set_rule(world.get_location("Box 7", player), lambda state: True)
    set_rule(world.get_location("Box 8", player), lambda state: True)
    set_rule(world.get_location("Box 9", player), lambda state: True)
    
    set_rule(world.get_location("Box 10", player), lambda state: True)
    set_rule(world.get_location("Box 11", player), lambda state: True)
    set_rule(world.get_location("Box 12", player), lambda state: True)
    set_rule(world.get_location("Box 13", player), lambda state: True)
    set_rule(world.get_location("Box 14", player), lambda state: True)
    
    set_rule(world.get_location("Box 15", player), lambda state: True)
    set_rule(world.get_location("Box 16", player), lambda state: True)
    set_rule(world.get_location("Box 17", player), lambda state: True)
    set_rule(world.get_location("Box 18", player), lambda state: True)
    set_rule(world.get_location("Box 19", player), lambda state: True)
    
    set_rule(world.get_location("Box 20", player), lambda state: True)
    set_rule(world.get_location("Box 21", player), lambda state: True)
    set_rule(world.get_location("Box 22", player), lambda state: True)
    set_rule(world.get_location("Box 23", player), lambda state: True)
    set_rule(world.get_location("Box 24", player), lambda state: True)

    world.completion_condition[player] = lambda state : state.has("Hero's Sword", player, 1) and state.has("Hero's Shield", player, 1) and state.has("Hero's Bow", player, 1)