"""
What are decorators?

In Python, a decorator is a special function that can be used to modify the behavior of another function.
Decorators are defined using the "@" symbol followed by the name of the decorator function, and they are 
applied to a function by placing them directly above the function definition.

"""

# decorator function


def decorator_func(func):
    def inner(a, b):
        if b == 0:
            print("oops can't devide...")
            return
        return func(a, b)
    return inner


# ordanry function
@decorator_func
def devide_func(a, b):
    return a/b


if __name__ == "__main__":
    dev = devide_func(5, 0)
    print(dev)
