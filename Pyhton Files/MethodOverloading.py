from multipledispatch import dispatch


@dispatch(int, int)
def product(a, b):
    return a * b


@dispatch(float, float, float)
def product(a, b, c):
    return a * b * c


@dispatch(int, float)
def product(a, b):
    return a * b


print(product(2.6, 3.8, 4.8))
print(product(2, 3.3))
print(product(2, 8))


class Example:
    def __init__(self):
        print("this Example constructer")

    def product_one(self, a: int, b: int):
        return a * b
