from typing import Generator, Callable, List
from functools import partial
from itertools import islice


def is_even(it: int) -> bool:
    #print(f"it is {it}")
    return it % 2 == 0


def add(x: int, y: int) -> int:
    #print(f"{x} and {y}")
    return x + y


add10: Callable[[int], int] = partial(add, 10)



def forloopyrange(start: int, end: int) -> Generator[int, None, None]:
    for it in range(start, end):
        if (is_even(it)):
            yield add10(it)


# very SQL
def expressionrange(start: int, end: int) -> Generator[int, None, None]:
    return (add10(it) for it in range(start, end) if is_even(it))


take_3_tolist = list(islice(forloopyrange(0, 20), 3))

take_3_tolist = list(islice(expressionrange(0, 20), 5))


def tolist_shortcut(start: int, end: int) -> List[int]:
    return [add10(it) for it in range(start, end) if is_even(it)]