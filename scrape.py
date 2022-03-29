import dns.name


fname = 'se.zone.txt'

names = set()

with open(fname, 'r') as f:
    for line in f:
        line = line.partition(';')[0].strip()

        #print(repr(line))

        if len(line) == 0:
            continue

        domain, *_ = line.split()

        #print(domain)#_

        name = str(dns.name.from_text(domain) - dns.name.from_text('se.'))

        names.add(name)

with open('se.names.txt', 'w') as f:
    for name in sorted(names):
        f.write(name + '\n')




