LAB_SOURCE_FILE=__file__


HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    # if n // 10 == 0:
    #     if n % 10 == 8:
    #         return 1
    #     return 0
    # if n % 10 == 8 :
    #     return 1 + num_eights(n // 10)
    # return num_eights(n // 10)  
    if n % 10 == 8 :
        return 1 + num_eights(n // 10)
    elif n < 10 :
        return 0
    else :
        return num_eights(n // 10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10 :
        return 0
    return abs(n % 10 - (n // 10) % 10 ) + digit_distance(n // 10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    """
    dist,prev = 0,n % 10
    n = n // 10
    while n :
        dist += abs(prev - n % 10)
        prev = n % 10
        n = n // 10
    return dist


def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    #note: 印象中貌似写某种递归代码时，一般都要写hepler function。
    #要不然不好写。最近的lab，disc,hw好多递归函数都是带个Helper function。
    #106B中也有好多带helper function的
    def interleaved_sum_helper(k):
        if k == n:
            return odd_func(k)
        if k == n - 1:
            return odd_func(k) + even_func(k + 1)
        return odd_func(k) + even_func(k + 1) + interleaved_sum_helper(k + 2)
    return interleaved_sum_helper(1)

    # def sum_from(k):
    #     if k > n:
    #         return 0
    #     elif k == n:
    #         return odd_func(k)
    #     return odd_func(k) + odd_func(k + 1) + sum_from(k + 2)
    # return sum_from(1)






def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1



#note: count_coins和count_partition其实基本一样，核心都是decision_tree
#每个路口都有两个选择，到底包不包含此时这个coin
#this is a tree_recursive function
def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    #keep in mind that helper function done the major job
#max版本，从大到小
    def count_coins_max(total,largest_coin) :
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif largest_coin == None:
            return 0
        else:   
        #其实说白了就只有两种组合，一种有max，一种没max
            return count_coins_max(total - largest_coin,largest_coin) + count_coins_max(total,next_smaller_coin(largest_coin)) 
        #经过分析，不需要担心total < 25的情况
    return count_coins_max(total,25)


#min版本，从小到大

    def count_coins_min(total,smallest_coin):
        if total == 0:
            return 1
        if total < 0:
            return 0
        if smallest_coin == None:
            return 0
        #说白了也是分两种情况。一种包含Min,一种不包含Min
        return count_coins_min(total - smallest_coin,smallest_coin) + count_coins_min(total,next_larger_coin(smallest_coin))
    return count_coins_min(total,1)








def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    #base case
    if n == 1:
        print_move(start,end)
    else :
        other = 6 - start - end
        move_stack(n - 1,start,other)
        print_move(start,end)
        move_stack(n - 1,other, end)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f:f(f))(lambda f : lambda x: 1 if x == 0 else x * f(f)(x - 1))

