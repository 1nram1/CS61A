def swipe(n):
    """Print the digits of n, one per line, 
    first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    >>> swipe(1911)
    1
    1
    9
    1
    9
    1
    1
    """
    if n < 10:
        print(n)
    else:
        "*** YOUR CODE HERE ***"
        #First print the first line of the output,
        #then make a recursive call, 
        #then print the last line of the output.
        print(n % 10)
        swipe(n // 10)
        print(n % 10)

def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...

    >>> skip_factorial(5) # 5 * 3 * 1
    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_factorial(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def is_prime_helper(i):
        "check whether no number from i up to n ** 0.5  evenly divides n."
        if i > (n ** 0.5):
            return True
        elif n % i == 0:
            return False
        else :
            return is_prime_helper(i + 1)
    return is_prime_helper(2)

def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)



def even(n):
    return 1 + hailstone(n // 2)

def odd(n):
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1 
    return 1 + hailstone(3 * n + 1)
  












def is_prime(n):
    assert n > 1
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True




def sevens(n, k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """

    """An effective approach to this problem is to simulate the game, stopping on turn n.
     The implementation must keep track of the final number n, the current number i, the player who will say i, 
     and the current direction that determines the next player (either increasing or decreasing).
     It works well to use integers to represent all of these, with direction switching between 1 (increase) and -1 (decreasing)."""


    def f(i, who, direction):
        if i == n:
            return who
        "*** YOUR CODE HERE ***"
        if has_seven(i) :
            direction = -1 * direction
            #direction = -direction
            who = ((who - 1 + k + direction) % k) + 1
            #who = who + direction
            #if who > k
            #   who = 1
            # if who < 1
            #     who = k

        return f(i + 1,who,direction)
    return f(1, 1, 1)

def sevens(n,k):
    """Return the (clockwise) position of who says n among k players.

    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    >>> sevens(18, 5)
    2
    """
    #类似循环队列，但要整体移动一位，让index起始为0
    #who - 1 :(0,k-1)
    who,direction = 1,1
    for i in range(1,n + 1,1):
        if i == n:
            return who
        if has_seven(i):
            direction = -1 * direction
        who = ((direction + who - 1 + k) % k) + 1

        
        



def has_seven(n):
    """ find out whether a number has the digit 7 or is a multiple of 7 recrusively"""
    if n == 0:
        return False
    elif n % 10 == 7 or n % 7 == 0:
        return True
    else:
        return has_seven(n // 10)



def count_partitions(n, m):
    """Count the ways to partition n using parts up to m.
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    """
# we need to specify the following base cases:
# There is one way to partition 0: include no parts.
# There are 0 ways to partition a negative n.
# There are 0 ways to partition any n greater than 0 using parts of size 0 or less
    
    #应对第一个递归调用的base case
    if n == 0:
        return 1
    elif n < 0:
        return 0
    #应对第二个递归调用的base case
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)
    
# note:We can think of a tree-recursive function as exploring different possibilities. 
# In this case, we explore the possibility that we use a part of size m and the possibility that we do not.
# The first and second recursive calls correspond to these possibilities.