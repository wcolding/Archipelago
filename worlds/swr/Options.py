from Options import Choice, Range, Toggle, DefaultOnToggle, DeathLink, dataclass, PerGameCommonOptions

class ProgressiveParts(Toggle):
    """Pod racer parts will always be the next level upgrade"""
    display_name = "Progressive Parts"

class ProgressiveCircuits(Toggle):
    """Access to circuits will be in the regular order"""
    display_name = "Progressive Circuits"
    
class EnableInvitationalCircuitPass(Toggle):
    """Affects how Invitational Circuit courses unlock. If enabled, Invitational is unlocked with a Circuit Pass item like the others. Otherwise, each Invitational course requires first place in all courses of a corresponding circuit."""
    display_name = "Invitational Circuit Behavior"

class StartingRacers(Choice):
    """Change which racers are available to use at the beginning"""
    display_name = "Starting Racers"
    option_vanilla = 0
    option_random_range = 1

class StartingRacersCount(Range):
    """How many random racers to start with. This option is only used if Starting Racers is set to 'random_range'"""
    display_name = "Number of Starting Racers"
    range_start = 1
    range_end = 6
    default = 6

class AIScaling(Choice):
    """Affects AI speed
    Vanilla: Courses use their default scaling
    Circuits: AI is scaled according to the current circuit
    Parts: AI is dynamically scaled according to the quality of your parts
    """
    display_name = "AI Scaling"
    option_vanilla = 0
    option_circuits = 1 
    option_parts = 2

class DisablePartDegradation(DefaultOnToggle):
    """Prevents parts from being damaged and removes pit droids from the item pool. The pit droid shop locations are disabled with this option as well"""
    display_name = "Disable Part Degradation"

@dataclass
class SWROptions(PerGameCommonOptions):
    progressive_parts: ProgressiveParts
    progressive_circuits: ProgressiveCircuits
    invitational_circuit_pass: EnableInvitationalCircuitPass
    starting_racers: StartingRacers
    starting_racers_count: StartingRacersCount
    disable_part_degradation: DisablePartDegradation
    ai_scaling: AIScaling
    deathlink: DeathLink