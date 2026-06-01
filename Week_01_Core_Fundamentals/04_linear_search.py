"""
TASK: 04 Linear Search

# Linear Search
Implement a linear search algorithm:
- Ask the user for a target value.
- Search a generated random list.
- Return the index or -1.
- Include `linear_search(values, target)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

import random

def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
numbers = []
for i in range(5):
    numbers.append(random.randint(1, 10))

print("List;", numbers)

target = input("Enter a number to search for")
