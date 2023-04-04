""" pass a function as a parameter to other functions python:

functions in programming languages are considered as objects, just like other data types 
such as strings and integers. As a result, functions can be passed around like any other object, 
allowing for powerful programming techniques

These functions are known as higher order functions..."""


def work_func(text):
    return text.upper()


def function(func):
    res = func("Python is scripting language")
    return res


if __name__ == "__main__":

    fun = function(work_func)
    print(fun)
