from BaseClasses import Item

class SWRacerItem(Item):
    game: str = "Star Wars Episode I Racer"


pod_progressive_item_table = {
    "Progressive Traction": 0,
    "Progressive Turning": 1,
    "Progressive Acceleration": 2,
    "Progressive Top Speed": 3,
    "Progressive Air Brake": 4,
    "Progressive Cooling": 5,
    "Progressive Repair": 6
 }

pod_traction_item_table = {
    "R-60 Repulsorgrip": 7,
    "R-80 Repulsorgrip": 8,
    "R-100 Repulsorgrip": 9,
    "R-300 Repulsorgrip": 10,
    "R-600 Repulsorgrip": 11
}

pod_turning_item_table = {
    "Control Shift Plate": 12,
    "Control Vectro Jet": 13,
    "Control Coupling": 14,
    "Control Nozzle": 15,
    "Control Stabilizer": 16 
}

pod_acceleration_item_table = {
    "44 PCX Injector": 17,
    "Dual 32PCX Injector": 18,
    "Quad 32PCX Injector": 19,
    "Quad 44PCX Injector": 20,
    "Mag-6 Injector": 21
}

pod_top_speed_item_table = {
    "Plug3 Thrust Coil": 22,
    "Plug5 Thrust Coil": 23,
    "Plug8 Thrust Coil": 24,
    "Block5 Thrust Coil": 25,
    "Block6 Thrust Coil": 26
}

pod_air_brake_item_table = {
    "Mark III Air Brake": 27,
    "Mark IV Air Brake": 28,
    "Mark V Air Brake": 29,
    "Tri-Jet Air Brake": 30,
    "Quadrijet Air Brake": 31
}

pod_cooling_item_table = {
    "Stack-3 Radiator": 32,
    "Stack-6 Radiator": 33,
    "Rod Coolant Pump": 34,
    "Dual Coolant Pump": 35,
    "Turbo Coolant Pump": 36
}

pod_repair_item_table = {
    "Dual Power Cell": 37,
    "Quad Power Cell": 38,
    "Cluster Power Plug": 39,
    "Rotary Power Plug": 40,
    "Cluster2 Power Plug": 41
}

pod_item_table = { **pod_traction_item_table, **pod_turning_item_table, **pod_acceleration_item_table, \
    **pod_top_speed_item_table, **pod_air_brake_item_table, **pod_cooling_item_table, **pod_repair_item_table }

racers_table = {
    # "Name":            [AP ID, Bitflag]
    "Anakin Skywalker":  [42, 0x00000001],
    "Teemto Pagalies":   [43, 0x00000002],
    "Sebulba":           [44, 0x00000004],
    "Ratts Tyerell":     [45, 0x00000008],
    "Aldar Beedo":       [46, 0x00000010],
    "Mawhonic":          [47, 0x00000020],
    "Ark 'Bumpy' Roose": [48, 0x00000040],
    "Wan Sandage":       [49, 0x00000080],
    "Mars Guo":          [50, 0x00000100],
    "Ebe Endocott":      [51, 0x00000200],
    "Dud Bolt":          [52, 0x00000400],
    "Gasgano":           [53, 0x00000800],
    "Clegg Holdfast":    [54, 0x00001000],
    "Elan Mak":          [55, 0x00002000],
    "Neva Kee":          [56, 0x00004000],
    "Bozzie Baranta":    [57, 0x00008000],
    "Boles Roor":        [58, 0x00010000],
    "Ody Mandrell":      [59, 0x00020000],
    "Fud Sang":          [60, 0x00040000],
    "Ben Quadrinaros":   [61, 0x00080000],
    "Slide Paramita":    [62, 0x00100000],
    "Toy Dampner":       [63, 0x00200000],
    "Bullseye Navior":   [64, 0x00400000]
}

vanilla_racers_list = {
    "Anakin Skywalker",
    "Ebe Endocott",
    "Dud Bolt",
    "Gasgano",
    "Elan Mak",
    "Ody Mandrell"
}

misc_item_table = {
    "Pit Droid": 65,
    "Semi Pro Circuit Pass": 66,
    "Galactic Circuit Pass": 67,
    "Invitational Circuit Pass": 68,
    "Progressive Circuit Pass": 69,
    #"400 Truguts": 70,
    #"600 Truguts": 71,
}

def get_item_table():
    item_table = { **pod_progressive_item_table, **pod_item_table, **misc_item_table }
    for racer in racers_table:
        item_table[racer] = racers_table[racer][0]

    return item_table

def get_offset_item_table(offset: int):
    item_table = get_item_table()
    for item in item_table:
        item_table[item] += offset 

    return item_table