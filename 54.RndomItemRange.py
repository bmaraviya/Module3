"""How can you pick a random item from a range?"""

import random
random_item = random.choice(list(range(1, 10)))
print(random_item)
random_item = random.randint(1, 9)
print(random_item)
