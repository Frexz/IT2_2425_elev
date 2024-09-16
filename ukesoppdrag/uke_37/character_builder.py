def main():
    # Oppgave a) - Fyll inn koden her
    
    # Oppgave d) - Fyll inn koden her

    # Oppgave e) - Fyll inn koden her

    # Oppgave h) - Fyll inn koden her
    
    # Oppgave i) - Fyll inn koden her
    pass

def print_sheet(char):
    print()
    for line in make_sheet(char):
        print(line)

def make_sheet(char):
    sheet = []
    stats = []
    sheet.append(f'{char["name"].center(49, "-")}')
    sheet.append(f'Level: {char["level"]:>42}')
    sheet.append(f'Armor Class: {char["armor"]:>36}')
    sheet.append(f'Hit Points: {char["hp"]:>37}')
    sheet.append(f'Speed: {char["speed"]:>38} ft.')
    sheet.append('-' * 49)
    sheet.append('|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |')
    sheet.append('|-------|-------|-------|-------|-------|-------|')
    stats.append(f'|{char["str"]:2} ({"+" if get_modifier(char["str"]) >= 0 else ""}{get_modifier(char["str"])})')
    stats.append(f'|{char["dex"]:2} ({"+" if get_modifier(char["dex"]) >= 0 else ""}{get_modifier(char["dex"])})')
    stats.append(f'|{char["con"]:2} ({"+" if get_modifier(char["con"]) >= 0 else ""}{get_modifier(char["con"])})')
    stats.append(f'|{char["int"]:2} ({"+" if get_modifier(char["int"]) >= 0 else ""}{get_modifier(char["int"])})')
    stats.append(f'|{char["wis"]:2} ({"+" if get_modifier(char["wis"]) >= 0 else ""}{get_modifier(char["wis"])})')
    stats.append(f'|{char["cha"]:2} ({"+" if get_modifier(char["cha"]) >= 0 else ""}{get_modifier(char["cha"])})|')
    sheet.append(''.join(stats))
    sheet.append('-' * 49)
    return sheet

def standard_array():
    # Oppgave b) - Fyll inn koden her
    pass

def roll_stats():
    # Oppgave c) - Fyll inn koden her
    pass

def choose_stat_generation():
    print('\nWelcome to this Dungeons & Dragons Character Creator.')
    print('Please choose between standard array and random generation for generating stats'
          'for your character.')
    # Oppgave d) - Fyll inn resten av koden her

def assign_stats(char, stats):
    abilities = ['str', 'dex', 'con', 'int', 'wis', 'cha']
    print("\nStats need to be assigned to your character's six abilities:")
    print('Strength (str), Dexterity (dex), Constitution (con), Intelligence (int), Wisdom (wis), and Charisma (cha)')
    print(f'\nStats to assign: {stats}')
    print(f'Abilities to assign to: {abilities}')

    # Oppgave e) - Fyll inn resten av koden her
    
    # Oppgave g) - Fyll inn koden her

def get_modifier(score):
    # Oppgave f) - Fyll inn koden her
    pass


main()