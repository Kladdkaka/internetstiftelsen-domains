from itertools import product
from string import ascii_lowercase

MIN_COUNT = 1
MAX_COUNT = 4

fname = 'se.names.txt'

with open(fname, 'r') as f:
    existing_names = set(filter(None, f.read().splitlines()))

f = open('data/result.txt', 'w')

for count in range(MIN_COUNT, MAX_COUNT + 1):
    combos = list(map(''.join, product(ascii_lowercase, repeat=count)))

    available = []

    for combo in combos:
        if combo not in existing_names:
            available.append(combo)
    
    print(f'Combos with {count} letters: {len(combos)}')
    print(f'Available/Total: {len(available)}/{len(combos)}')

    f.write('############################################\n')
    f.write(f'Combos with {count} letters:\n')
    f.write(', '.join(available) + '\n')


