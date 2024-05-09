def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    def paths_helper(i,j):
        if j == n or i == m:
            return 1
        # if j == n :
        #     return 1
        #     #return paths_helper(i + 1,j)
        # if i == m :
        #     return 1
        #     #return paths_helper(i,j + 1)
        return paths_helper(i + 1,j) + paths_helper(i,j + 1)
    return paths_helper(1,1)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1:
        return 1
    return paths(m - 1,n) + paths(m,n - 1)


def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    # if not len(s) :
    if s == []:
        return 1
    if len(s) == 1:
        return s[0]
    #return max(s[0] * max_product(s[2:]),max_product(s[1:])) 
    return max(s[0] * max_product(s[2:]),s[1] * max_product(s[3:]))

#note:边界情况：考虑问题的边界条件。
#例如，对于数组或列表的操作（如排序、查找等），
#往往当数组为空或只有一个元素时，会作为基本情况。

# 下面是一些选择递归基本情况的一般性原则和技巧：
# 理解问题的性质：首先，你需要深入理解你正在解决的问题的性质。
#你需要找出存在直接解决方案的最简单的问题实例。例如，在二分查找中，如果搜索空间为空，你就知道该元素不存在于数组中。
# 边界情况：考虑问题的边界条件。例如，对于数组或列表的操作（如排序、查找等），
#往往当数组为空或只有一个元素时，会作为基本情况。又如求解阶乘 n!，0! 和 1! 是显然的基本情况。
# 将大问题简化：考虑如何将大问题简化为小问题。你的递归函数应该试图将问题简化为更小、更容易解决的形式，
#直到它变得足够简单以至于可以直接解决。例如，计算斐波那契数列的问题可以简化为计算两个更小的斐波那契数列的问题，直到问题简化为计算 fib(0) 和 fib(1) —— 这就是基本情况。
# 递归终止：递归必须有终止条件。当这个条件满足时，递归函数会直接返回一个值，而不再进行递归调用。这就是递归的基本情况。
#例如，对于树或图的遍历，如果当前节点是空的，则没有必要再进行递归遍历，此时空节点就是基本情况。


def sums(n, m):
    """Return lists that sum to n containing positive numbers up to m that
    have no adjacent repeats.(no adjacent is the key)

    >>> sums(5, 1)
    []
    >>> sums(5, 2)
    [[2, 1, 2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    >>> sums(5, 5)
    [[1, 3, 1], [1, 4], [2, 1, 2], [2, 3], [3, 2], [4, 1], [5]]
    >>> sums(6, 3)
    [[1, 2, 1, 2], [1, 2, 3], [1, 3, 2], [2, 1, 2, 1], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    if n < 0:
        return []
    if n == 0 :
        sums_to_zero = []
        return [sums_to_zero]
    result = []
    for k in range(1,m + 1):
        result = result + [[k] + rest for rest in sums(n - k) if rest == [] or rest[0] != k]
