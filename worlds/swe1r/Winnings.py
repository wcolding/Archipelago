from enum import IntEnum

class Difficulty(IntEnum):
    Fair = 0
    Skilled = 1
    WTA = 2

amateur_fair = [800, 700, 600, 100]
amateur_skilled = [1200, 600, 300, 100]
amateur_wta = [2200]

semipro_fair = [int(val * 1.5) for val in amateur_fair]
semipro_skilled = [int(val * 1.5) for val in amateur_skilled]
semipro_wta = [int(val * 1.5) for val in amateur_wta]

galactic_fair = [int(val * 2) for val in amateur_fair]
galactic_skilled = [int(val * 2) for val in amateur_skilled]
galactic_wta = [int(val * 2) for val in amateur_wta]

invitational_fair = [2000, 1750, 1500]
invitational_skilled = [3000, 1500, 750]
invitational_wta = [5500]

difficulty_map = [
    [amateur_fair, semipro_fair, galactic_fair, invitational_fair],
    [amateur_skilled, semipro_skilled, galactic_skilled, invitational_skilled],
    [amateur_wta, semipro_wta, galactic_wta, invitational_wta]
]

def get_balanced_winnings(circuit_vals: list, count: int):
    packed_list = []
    while (len(packed_list) < count):
        packed_list += circuit_vals

    trim_amt = len(packed_list) - count
    packed_list = packed_list[0:len(packed_list) - trim_amt]
    return packed_list

def get_full_winnings(difficulty: Difficulty):
    winnings = []
    winnings += get_balanced_winnings(difficulty_map[difficulty][0], 7)
    winnings += get_balanced_winnings(difficulty_map[difficulty][1], 7)
    winnings += get_balanced_winnings(difficulty_map[difficulty][2], 7)
    winnings += get_balanced_winnings(difficulty_map[difficulty][3], 4)
    return winnings

def get_money_item_name(amount: int):
    return '{value} Truguts'.format(value = amount)

def generate_money_item_table(starting_id: int):
    combined_winnings = amateur_fair + amateur_skilled + amateur_wta \
        + semipro_fair + semipro_skilled + semipro_wta \
        + galactic_fair + galactic_skilled + galactic_wta \
        + invitational_fair + invitational_skilled + invitational_wta
    
    condensed_winnings = []

    for entry in combined_winnings:
        if entry not in condensed_winnings:
            condensed_winnings += [entry]

    condensed_winnings.sort()
    current_id = starting_id
    table = {}
    for single_entry in condensed_winnings:
        table[get_money_item_name(single_entry)] = current_id
        current_id += 1
    
    return table
    
def print_generated_money_items(starting_id: int):
    table = generate_money_item_table(starting_id)
    print()
    print("{")
    for item in table:
        print(f'\t\"{item}\": {table[item]},')
    print("}")

#print_generated_money_items(70)