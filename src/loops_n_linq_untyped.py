# type: ignore
from typing import Generator, List
from itertools import islice
from function import add10, is_even


def forloopyrange(start, end):
    for it in range(start, end):
        if (is_even(it)):
            yield add10(it)


# very SQL
def expressionrange(start, end):
    return (add10(it) for it in range(start, end) if is_even(it))


take_3_tolist = list(islice(forloopyrange(0, 20), 3))

take_5_tolist = list(islice(expressionrange(0, 20), 5))

print(take_3_tolist)
print(take_5_tolist)


def tolist_shortcut(start, end):
    return [add10(it) for it in range(start, end) if is_even(it)]