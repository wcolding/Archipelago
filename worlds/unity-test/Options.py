import typing
from Options import Option, DefaultOnToggle, Range, Toggle

class RedBoxes(DefaultOnToggle):
    display_name = "Red Boxes"
    
class BlueBoxes(DefaultOnToggle):
    display_name = "Blue Boxes"
    
class GreenBoxes(DefaultOnToggle):
    display_name = "Green Boxes"

UT_options: typing.Dict[str,type[Option]] = {
    "RedBoxes": RedBoxes,
    "BlueBoxes": BlueBoxes,
    "GreenBoxes": GreenBoxes
} 