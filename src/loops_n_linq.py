from typing import Generator, List
from itertools import islice
from function import add10, is_even




def forloopyrange(start: int, end: int) -> Generator[int, None, None]:
    for it in range(start, end):
        if (is_even(it)):
            yield add10(it)


# very SQL
def expressionrange(start: int, end: int) -> Generator[int, None, None]:
    return (add10(it) for it in range(start, end) if is_even(it))


take_3_tolist = list(islice(forloopyrange(0, 20), 3))

take_5_tolist = list(islice(expressionrange(0, 20), 5))

print(take_3_tolist)
print(take_5_tolist)


def tolist_shortcut(start: int, end: int) -> List[int]:
    return [add10(it) for it in range(start, end) if is_even(it)]