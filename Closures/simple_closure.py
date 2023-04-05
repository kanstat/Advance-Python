"""Closures: These are nested functions i.e functions inside functions, and inner functions 
are able to access the variables of outer functions even after outer function is closed"""


def outer_func(y):
    def inner(x):
        res = x*y
        return res
    return inner


if __name__ == "__main__":
    obj = outer_func(10)
    res = obj(10)
    print(res)
