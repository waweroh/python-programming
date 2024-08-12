import sys
import random
import pyjokes


random_int = random.randint(1, 10)
print(random_int)

joke = pyjokes.get_joke('en', 'neutral')
print(joke)