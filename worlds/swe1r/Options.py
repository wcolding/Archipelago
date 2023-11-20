import typing
from Options import Option, Choice, Range, DefaultOnToggle

class StartingRacers(Choice):
    """Change which racers are available to use at the beginning"""
    display_name = "Starting Racers"
    option_vanilla = 0
    option_random_one = 1
    option_random_range = 2

class NumberOfStartingRacers(Range):
    """How many random racers to start with. This option is only used if Starting Racers is set to 'random_range'"""
    range_start = 2
    range_end = 5
    default = 5

class DisablePartDegradation(DefaultOnToggle):
    """Prevents parts from being damaged and removes pit droids from the item pool. The pit droid shop locations are disabled with this option as well"""
    display_name = "Disable Part Degradation"

class RequiredPlacement(Choice):
    """Minimum place you are required to get on a track to check the location. Note that you will still be able to progress within a circuit with 4th or better"""
    option_first = 0
    option_second = 1
    option_third = 2