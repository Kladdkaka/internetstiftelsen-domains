import requests
import re
import validators

# ugly :D
def decider(word: str) -> bool:
    if not validators.domain(word + '.se'):
        return False

    if word.encode("idna").decode() != word: # lol
        return False

    return True


raw_text = requests.get('https://raw.githubusercontent.com/almgru/svenska-ord.txt/master/svenska-ord.txt').text
all_words = set(filter(None, raw_text.splitlines()))

all_words = list(filter(decider, map(str.lower, all_words)))



with open('data/wordlist.txt', 'w', encoding='utf-8') as f:
    for name in sorted(all_words):
        f.write(name + '\n')
