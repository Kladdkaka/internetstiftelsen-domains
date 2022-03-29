import requests
from ratelimit import limits, RateLimitException, sleep_and_retry
from concurrent.futures import ThreadPoolExecutor as PoolExecutor

SECOND = 1
MAX_CALLS_PER_SECOND = 34

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_SECOND, period=SECOND)
def get_domain_status(name):
    r = requests.get(f'http://free.iis.se/free?q={name}.se')
    domain, status = r.text.split()
    return domain, status


with open('data/names.txt', 'r') as f:
    names_to_check = set(filter(None, f.read().splitlines()))

with PoolExecutor(max_workers=3) as executor:
    for domain, status in executor.map(get_domain_status, names_to_check):
        print(domain, status)