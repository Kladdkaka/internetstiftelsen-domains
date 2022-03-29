fname = 'se.zone.txt'

names = set()

with open(fname, 'r') as f:
    for line in f:
        line = line.partition(';')[0].strip()

        if len(line) == 0:
            continue

        domain, *_ = line.split()
        domain = domain[:-1] # remove trailing dot

        domain = domain.split('.')

        if len(domain) == 1: # top level, ignore
            continue
        
        name = domain[-2]
        names.add(name)

with open('se.names.txt', 'w') as f:
    for name in sorted(names):
        f.write(name + '\n')




