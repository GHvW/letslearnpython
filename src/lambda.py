
from typing import TypeVar, Callable, Iterable

A = TypeVar("A")
B = TypeVar("B")

def select(fn: Callable[[A], B], list: Iterable[A]) -> Iterable[B]:
    return map(fn, list)


result: Iterable[int] = select(lambda x: x * 100, [1, 2, 3, 4, 5])

printable = list(result)

print(printable)
