# Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints: Consider use yield

from itertools import count


class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

n_value = 720
divisible_by_seven_instance = DivisibleBySevenGenerator(n_value)
countything = 1

for num in divisible_by_seven_instance.generate_divisible_by_seven():
    print(f"#{countything} : {num}")
    countything += 1
