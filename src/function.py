from typing import Callable
from functools import partial

def generate_greeting(kind: str) -> str:
    if kind == "Texan":
        return "Howdy!"
    elif kind == "Spanish":
        return "Hola"
    elif kind == "New Yorker":
        return ""
    else:
        return "Hello"


def is_even(it: int) -> bool:
    return it % 2 == 0


def add(x: int, y: int) -> int:
    return x + y


add10: Callable[[int], int] = partial(add, 10)

print(add10(100))
print(is_even(102))
