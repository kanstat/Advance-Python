
'''Assign a function to multiple variables'''


def func(string):
    return string.lower()


"""When you assign a function to a variable, you are not creating a copy of the function.
Instead, each variable is simply a reference to the same function object. This means that 
if you modify the function using one variable, the changes will be visible when you call 
the function using any of the other variables."""
if __name__ == "__main__":

    var1 = func
    print(var1('KANCHAN'))
    var2 = func
    print(var2('SHARMA'))

    var1.custom_attri = "This is custom"
    print(var2.custom_attri)

    print(id(var1))
    print(id(var2))
