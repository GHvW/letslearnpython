# type: ignore
from functools import partial


def generate_greeting(kind):
    if kind == "Texan":
        return "Howdy!"
    elif kind == "Dude":
        return "Sup Bro"
    elif kind == "New Yorker":
        return ""
    else:
        return "Hello"


def is_even(it):
    return it % 2 == 0


def add(x, y):
    return x + y


add10 = partial(add, 10)

result1 = add10(100)
result2 = is_even(102)

print(result1)
print(result2)