from BaseClasses import Location

class UTLocation(Location):
    game: str = "Unity Test"

locRed = {
    "Box 0": 252100,
    "Box 4": 252104,
    "Box 6": 252106,
    "Box 10": 252110,
    "Box 12": 252112,
    "Box 16": 252116,
    "Box 18": 252118,
    "Box 22": 252122,
    "Box 24": 252124
}

locBlue = {
    "Box 1": 252101,
    "Box 3": 252103,
    "Box 7": 252107,
    "Box 9": 252109,
    "Box 13": 252113,
    "Box 15": 252115,
    "Box 19": 252119,
    "Box 21": 252121
}


locGreen = {
    "Box 2": 252102,
    "Box 5": 252105,
    "Box 8": 252108,
    "Box 11": 252111,
    "Box 14": 252114,
    "Box 17": 252117,
    "Box 20": 252120,
    "Box 23": 252123
}

location_table = {**locRed, **locBlue, **locGreen}