from BaseClasses import MultiWorld
from .Options import ProgressiveCircuits, InvitationalCircuitBehavior

def check_progressive_circuits(world: MultiWorld, player: int, required: int) -> bool:
    return world.state.has("Progressive Circuit Pass", player, required)

def semipro_unlocked(world: MultiWorld, player: int) -> bool:
    if (world.progressive_circuits[player].value):
        return check_progressive_circuits(world, player, 1)
    else:
        return world.state.has("Semi Pro Circuit Pass", player)

def galactic_unlocked(world: MultiWorld, player: int) -> bool:
    if (world.progressive_circuits[player].value):
        return check_progressive_circuits(world, player, 2)
    else:
        return world.state.has("Galactic Circuit Pass", player)

def invitational_unlocked(world: MultiWorld, player: int) -> bool:
    if (world.invitational_circuit_behavior[player].value == InvitationalCircuitBehavior.option_circuit_pass):
        if (world.progressive_circuits[player].value):
            return check_progressive_circuits(world, player, 3)
        else:
            return world.state.has("Invitational Circuit Pass", player)
    else:
        # todo: check locations
        return False

def pit_shop_available(world: MultiWorld, player: int) -> bool:
    return (world.disable_part_degradation[player].value == 0)