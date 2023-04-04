'''
Function inside Function

Inner functions can be used to create encapsulated code that only needs to be used within a specific context.
They can also be used to implement closures, which are functions that have access to variables from their enclosing 
scope, even after that scope has been destroyed.

'''


def outer_func():
    def inner_func():
        print("Hello from inner func")
    inner_func()


o = outer_func()

####################################################################################

'''The core feature of inner functions is their ability to access variables and objects
from their enclosing function even after this function has returned. The enclosing function
provides a namespace that is accessible to the inner function ---real python'''

# name is nonlocal parameter from the point of view of innerfunc


def outer_func1(name):
    def inner_fun():
        print(f"Hello from inner function '{name}'")
    inner_fun()


out = outer_func1("Pythonista")

#########################################################################################


def outer_odd_even(val):
    if not isinstance(val, int):
        raise TypeError("oops, number should be int type")
    if val < 0:
        raise ValueError("number should be greater than zero or zero ")

    def inner_odd_even():
        if val % 2 == 0:
            print("given number is even")
            return
        print("number is odd")
    inner_odd_even()


even_odd = outer_odd_even('-1')


'''UseCases: Encapsulation, Decorators, Closures, Helping inner functions etc..'''
