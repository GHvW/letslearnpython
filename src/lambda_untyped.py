# type: ignore

def select(fn, list):
    return map(fn, list)

result = select(lambda x: x * 100, [1, 2, 3, 4, 5])

printable = list(result)

print(printable)

