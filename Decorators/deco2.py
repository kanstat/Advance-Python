# adding functionality through decorator to print the funcs full name..
def print_full_name(func):
    def inner(num):
        print(
            f"The full name of function that gives the sum of given number '{func.__name__}'")
        return func(num)
    return inner

# ordnary function that gives the sum of given numbers


# @print_full_name
def sum_func(number):
    sum = 0
    i = 0
    while i <= number:
        sum += i
        i = i+1
    return f"The sum of given number {number} is '{sum}'"


if __name__ == "__main__":
    # s = sum_func(10)
    # print(s)

    pr = print_full_name(sum_func)
    print(pr(10))
