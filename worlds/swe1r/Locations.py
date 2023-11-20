from BaseClasses import Location

class SWRacerLocation(Location):
    game: str = "Star Wars Episode I Racer"

wattos_shop_table = {
    "Watto's Shop - Traction Upgrade 1": 100,
    "Watto's Shop - Traction Upgrade 2": 101,
    "Watto's Shop - Traction Upgrade 3": 102,
    "Watto's Shop - Traction Upgrade 4": 103,
    "Watto's Shop - Traction Upgrade 5": 104,
    
    "Watto's Shop - Turning Upgrade 1": 105,
    "Watto's Shop - Turning Upgrade 2": 106,
    "Watto's Shop - Turning Upgrade 3": 107,
    "Watto's Shop - Turning Upgrade 4": 108,
    "Watto's Shop - Turning Upgrade 5": 109,
    
    "Watto's Shop - Acceleration Upgrade 1": 110,
    "Watto's Shop - Acceleration Upgrade 2": 111,
    "Watto's Shop - Acceleration Upgrade 3": 112,
    "Watto's Shop - Acceleration Upgrade 4": 113,
    "Watto's Shop - Acceleration Upgrade 5": 114,
    
    "Watto's Shop - Top Speed Upgrade 1": 115,
    "Watto's Shop - Top Speed Upgrade 2": 116,
    "Watto's Shop - Top Speed Upgrade 3": 117,
    "Watto's Shop - Top Speed Upgrade 4": 118,
    "Watto's Shop - Top Speed Upgrade 5": 119,
    
    "Watto's Shop - Air Brake Upgrade 1": 120,
    "Watto's Shop - Air Brake Upgrade 2": 121,
    "Watto's Shop - Air Brake Upgrade 3": 122,
    "Watto's Shop - Air Brake Upgrade 4": 123,
    "Watto's Shop - Air Brake Upgrade 5": 124,
    
    "Watto's Shop - Cooling Upgrade 1": 125,
    "Watto's Shop - Cooling Upgrade 2": 126,
    "Watto's Shop - Cooling Upgrade 3": 127,
    "Watto's Shop - Cooling Upgrade 4": 128,
    "Watto's Shop - Cooling Upgrade 5": 129,
    
    "Watto's Shop - Repair Upgrade 1": 130,
    "Watto's Shop - Repair Upgrade 2": 131,
    "Watto's Shop - Repair Upgrade 3": 132,
    "Watto's Shop - Repair Upgrade 4": 133,
    "Watto's Shop - Repair Upgrade 5": 134,
}

junkyard_table = {
    "Junkyard - Item 1": 135,
    "Junkyard - Item 2": 136,
    "Junkyard - Item 3": 137,
    "Junkyard - Item 4": 138,
    "Junkyard - Item 5": 139,
    "Junkyard - Item 6": 140,
    "Junkyard - Item 7": 141,
}

pit_droid_shop_table = {
    "Pit Droid Shop - 1st Droid": 142,
    "Pit Droid Shop - 2nd Droid": 143,
    "Pit Droid Shop - 3rd Droid": 144
}

course_clears_amateur_table = {
    "Amateur 1": 145,
    "Amateur 2": 146,
    "Amateur 3": 147,
    "Amateur 4": 148,
    "Amateur 5": 149,
    "Amateur 6": 150,
    "Amateur 7": 151
}

course_clears_semipro_table = {
    "Semipro 1": 152,
    "Semipro 2": 153,
    "Semipro 3": 154,
    "Semipro 4": 155,
    "Semipro 5": 156,
    "Semipro 6": 157,
    "Semipro 7": 158
}

course_clears_galactic_table = {
    "Galactic 1": 159,
    "Galactic 2": 160,
    "Galactic 3": 161,
    "Galactic 4": 162,
    "Galactic 5": 163,
    "Galactic 6": 164,
    "Galactic 7": 165
}

course_clears_invitational_table = {
    "Invitational 1": 166,
    "Invitational 2": 167,
    "Invitational 3": 168,
    "Invitational 4": 169
}

racer_unlocks_table = {
    "Racer Unlock - Mon Gazza Speedway": 170,
    "Racer Unlock - The Boonta Classic": 171,
    "Racer Unlock - Howler Gorge": 172,
    "Racer Unlock - Beedo's Wild Ride": 173,
    "Racer Unlock - Andobi Mountain Run": 174,
    "Racer Unlock - Bumpy's Breakers": 175,
    "Racer Unlock - Scrapper's Run": 176,
    "Racer Unlock - Spice Mine Run": 177,
    "Racer Unlock - Aquilaris Classic": 178,
    "Racer Unlock - Baroo Coast": 179,
    "Racer Unlock - Abyss": 180,
    "Racer Unlock - Zugga Challenge": 181,
    "Racer Unlock - Vengeance": 182,
    "Racer Unlock - Inferno": 183,
    "Racer Unlock - Ando Prime Centrum": 184,
    "Racer Unlock - Executioner": 185,
    "Racer Unlock - Sunken City": 186,
}

location_table = { **wattos_shop_table, **junkyard_table, **pit_droid_shop_table, **course_clears_amateur_table, \
    **course_clears_semipro_table, **course_clears_galactic_table, **course_clears_invitational_table, **racer_unlocks_table }

def get_offset_location_table(offset: int):
    offset_loc_table = location_table
    for loc in offset_loc_table:
        offset_loc_table[loc] += offset 

    return offset_loc_table