# def is_prime(n):
#     return n>1 and smallest_factor(n)==n
#
# def smallest_factor(n):
#     k=2
#     while k<=n:
#         if n%k==0:
#             return k
#         k+=1
#
# def print_factors(n):
#     while n>1:
#         f=smallest_factor(n)
#         print(f)
#         n=n // f

# print(print_factors(21))
from operator import add


def twenty_twenty_one():
    return 2021


print(twenty_twenty_one())

# def add_func(f,g):
#     # def adder(x):
#     #     return f(x)+g(x)
#     # return adder
#     return lambda x:f(x)+g(x)
#
# from math import sin,cos,pi
#
# h=add_func(sin,cos)
# print(h(pi/3))

from math import sin,cos,pi
def combine_func(op):
    def combined(f, g):
        def val(x):
            return op(f(x),g(x))
        return val
    return combined

add_func=combine_func(lambda x,y:x+y)
h=add_func(sin,cos)
print(h(pi/2))

