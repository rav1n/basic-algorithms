"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    """ Algorithm:
    1. If position matches with base cases(0 and 1) then
        return the position. i.e.
        1.1 If position == 0
                return 0
        1.2 If position == 1
                return 1
    2. Else return addition of previous two values
    """
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)

    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
