import typing
from Options import Option, DeathLink, Range, Toggle, DefaultOnToggle, Choice

class Dungeons(DefaultOnToggle):
    """This controls whether dungeons can contain progress items."""
    display_name = "Dungeons"

class PuzzleSecretCaves(DefaultOnToggle):
    """This controls whether puzzle-focused secret caves can contain progress items."""
    display_name = "Puzzle Secret Caves"

class CombatSecretCaves(Toggle):
    """This controls whether combat-focused secret caves (besides Savage Labyrinth) can contain progress items."""
    display_name = "Combat Secret Caves"
    
class SavageLabyrinth(Toggle):
    """This controls whether the Savage Labyrinth can contain progress items."""
    display_name = "Savage Labyrinth"
    
class GreatFairies(DefaultOnToggle):
    """This controls whether the items given by Great Fairies can be progress items."""
    display_name = "Great Fairies"
    
class FreeGifts(DefaultOnToggle):
    """This controls whether gifts freely given by NPCs can be progress items (Tott, Salvage Corp, imprisoned Tingle)."""
    display_name = "Free Gifts"
    
class Miscellaneous(DefaultOnToggle):
    """Miscellaneous locations that don't fit into any of the above categories (outdoors chests, wind shrine, Cyclos, etc)."""
    display_name = "Miscellaneous"

class TingleChests(Toggle):
    """Tingle Chests that are hidden in dungeons and must be bombed to make them appear. (2 in DRC, 1 each in FW, TotG, ET, and WT)."""
    display_name = "Tingle Chests"
    
class ShortSidequests(Toggle):
    """This controls whether sidequests that can be completed quickly can reward progress items."""
    display_name = "Short Sidequests"
    
class LongSidequests(Toggle):
    """This controls whether long sidequests (e.g. Lenzo's assistant, withered trees, goron trading) can reward progress items."""
    display_name = "Long Sidequests"
    
class SpoilsTrading(Toggle):
    """This controls whether the items you get by trading in spoils to NPCs can be progress items."""
    display_name = "Spoils Trading"
    
class Mail(Toggle):
    """This controls whether mail can contain progress items."""
    display_name = "Mail"
    
class Minigames(Toggle):
    """This controls whether most minigames can reward progress items (auctions, mail sorting, barrel shooting, bird-man contest)."""
    display_name = "Minigames"
    
class BattlesquidMinigame(Toggle):
    """This controls whether the Windfall battleship minigame can reward progress items."""
    display_name = "Battlesquid Minigame"
    
class ExpensivePurchases(DefaultOnToggle):
    """This controls whether items that cost a lot of rupees can be progress items (Rock Spire shop, auctions, Tingle's letter, trading quest)."""
    display_name = "Expensive Purchases"
    
class IslandPuzzles(Toggle):
    """This controls whether various island puzzles can contain progress items (e.g. chests hidden in unusual places)."""
    display_name = "Island Puzzles"

class PlatformsRafts(Toggle):
    """This controls whether lookout platforms and rafts can contain progress items."""
    display_name = "Lookout Platforms and Rafts"
    
class Submarines(Toggle):
    """This controls whether submarines can contain progress items."""
    display_name = "Submarines"
    
class BigOctosGunboats(Toggle):
    """This controls whether the items dropped by Big Octos and Gunboats can contain progress items."""
    display_name = "Big Octos and Gunboats"
    
class EyeReefChests(Toggle):
    """This controls whether the chests that appear after clearing out the eye reefs can contain progress items."""
    display_name = "Eye Reef Chests"
    
class TriforceCharts(Toggle):
    """This controls whether the sunken treasure chests marked on Triforce Charts can contain progress items."""
    display_name = "Sunken Treasure (From Triforce Charts)"
    
class TreasureCharts(Toggle):
    """This controls whether the sunken treasure chests marked on Treasure Charts can contain progress items."""
    display_name = "Sunken Treasure (From Treasure Charts)"

class SwordMode(Choice):
    """Controls whether you start with the Hero's Sword, the Hero's Sword is randomized, or if there are no swords in the entire game.\nSwordless and No Starting Sword are challenge modes, not recommended for your first run. Also, FF's Phantom Ganon is vulnerable to Skull Hammer in Swordless mode only."""
    display_name = "Sword Mode"
    option_startwith = 0
    option_startwithout = 1
    option_swordless = 2

class RandomizeEntrances(Choice):
    """Shuffles around which dungeon entrances/secret cave entrances take you into which dungeons/secret caves.\n(No effect on Forsaken Fortress or Ganon's Tower.)"""
    display_name = "Randomize Entrances"
    option_disabled = 0
    option_dungeons = 1
    option_caves = 2
    option_dungeons_caves_separate = 3
    option_dungeons_caves_together = 4