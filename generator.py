import random
import string

def infinite_random_letters():
    while True:
        yield random.choice(string.ascii_lowercase)

# Приклад використання (показати перші 20)
gen = infinite_random_letters()
for _ in range(20):
    print(next(gen), end=" ")
