# from operator import add, sub
#
#
# def a_plus_abs_b(a, b):
#     """Return a+abs(b), but without calling abs.
#
#     >>> a_plus_abs_b(2, 3)
#     5
#     >>> a_plus_abs_b(2, -3)
#     5
#     >>> # a check that you didn't change the return statement!
#     >>> import inspect, re
#     >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
#     ['return f(a, b)']
#     """
#     if b < 0:
#         f =sub
#     else:
#         f =add
#     return f(a, b)
#
# print(a_plus_abs_b(3,-2))

#
# def two_of_three(x, y, z):
#     """Return a*a + b*b, where a and b are the two smallest members of the
#     positive numbers x, y, and z.
#
#     >>> two_of_three(1, 2, 3)
#     5
#     >>> two_of_three(5, 3, 1)
#     10
#     >>> two_of_three(10, 2, 8)
#     68
#     >>> two_of_three(5, 5, 5)
#     50
#     >>> # check that your code consists of nothing but an expression (this docstring)
#     >>> # a return statement
#     >>> import inspect, ast
#     >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
#     ['Expr', 'Return']
#     """
#     return min(x,y,z)**2+(x+y+z-min(x,y,z)-max(x,y,z))**2
#
# print(two_of_three(-1,-2,-3))


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    k=n-1
    while k>=1:
        if n%k==0 :
            return k
        k=k-1

# print(largest_factor(15))
# print(largest_factor(80))
# print(largest_factor(13))
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 'equal', 'not equal')
    'not equal'
    >>> if_function(3>2, 'bigger', 'smaller')
    'bigger'
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    61A
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():
    """
    >>> result = with_if_function()
    Welcome to
    61A
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(), false_func())


def cond():
    "*** YOUR CODE HERE ***"


def true_func():
    "*** YOUR CODE HERE ***"


def false_func():
    "*** YOUR CODE HERE ***"


# def hailstone(n):
#     """Print the hailstone sequence starting at n and return its
#     length.
#
#     >>> a = hailstone(10)
#     10
#     5
#     16
#     8
#     4
#     2
#     1
#     >>> a
#     7
#     """
#     "*** YOUR CODE HERE ***"

#
# def func(x):
#     x+=1
#
# y=3
# func(y)
# print(y)

def sum_squares(N):
    if N<1:
        return 0
    else:
        return N**2+sum_squares(N-1)

# print(sum_squares(3))
# print(sum_squares(4))

def f(x):
    def g(y):
        x=y
    g(4)
    return x

def print_sum(n):
    print(n)
    def next_sum(k):
        return print_sum(n+k)
    return next_sum
print(print_sum(1))