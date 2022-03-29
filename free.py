import requests
from ratelimit import limits, RateLimitException, sleep_and_retry
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

SECOND = 1
MAX_CALLS_PER_SECOND = 34

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_SECOND, period=SECOND)
def get_domain_status(name):
    r = requests.get(f'http://free.iis.se/free?q={name}.se')
    status, domain = r.text.split()
    return domain, status

with open('se.names.txt', 'r') as f:
    names_that_exists_from_zonefile = set(filter(None, f.read().splitlines()))


with open('data/wordlist.txt', 'r') as f:
    names_to_check = set(filter(None, f.read().splitlines()))

print(f'Names to check: {len(names_to_check)}')
names_to_check = [name for name in names_to_check if name not in names_that_exists_from_zonefile]
print(f'Names to check after first filtering: {len(names_to_check)}')

with PoolExecutor(max_workers=3) as executor:
    for domain, status in executor.map(get_domain_status, names_to_check):
        if status == 'occupied':
            continue

        print(domain, status)