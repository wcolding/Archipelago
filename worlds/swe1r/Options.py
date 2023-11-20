import typing
from Options import Option, Choice, Range, Toggle, DefaultOnToggle

class ProgressiveParts(Toggle):
    """Pod racer parts will always be the next level upgrade"""
    display_name = "Progressive Parts"

class ProgressiveCircuits(Toggle):
    """Access to circuits will be in the regular order"""
    display_name = "Progressive Circuits"
    
class InvitationalCircuitBehavior(Choice):
    """Affects how Invitational Circuit courses unlock. Vanilla behavior requires first place in all courses of a circuit per invitational course. Circuit pass treats it like the other circuits (unlocked with a Circuit Pass item)"""
    display_name = "Invitational Circuit Behavior"
    option_vanilla = 0
    option_circuit_pass = 1

class StartingRacers(Choice):
    """Change which racers are available to use at the beginning"""
    display_name = "Starting Racers"
    option_vanilla = 0
    option_random_one = 1
    option_random_range = 2

class NumberOfStartingRacers(Range):
    """How many random racers to start with. This option is only used if Starting Racers is set to 'random_range'"""
    display_name = "Number of Starting Racers"
    range_start = 2
    range_end = 5
    default = 5

class DisablePartDegradation(DefaultOnToggle):
    """Prevents parts from being damaged and removes pit droids from the item pool. The pit droid shop locations are disabled with this option as well"""
    display_name = "Disable Part Degradation"

class RequiredPlacement(Choice):
    """Minimum place you are required to get on a track to check the location. Note that you will still be able to progress within a circuit with 4th or better"""
    display_name = "Required Placement"
    option_first = 0
    option_second = 1
    option_third = 2

swr_options = {
    "progressive_parts": ProgressiveParts,
    "progressive_circuits": ProgressiveCircuits,
    "invitational_circuit_behavior": InvitationalCircuitBehavior,
    "starting_racers": StartingRacers,
    "number_of_starting_racers": NumberOfStartingRacers,
    "disable_part_degradation": DisablePartDegradation,
    "required_placement": RequiredPlacement
}