HW_SOURCE_FILE=__file__


def insert_items(s, before, after):
    """Insert after into s after each occurrence of before and then return s.

    >>> test_s = [1, 5, 8, 5, 2, 3]
    >>> new_s = insert_items(test_s, 5, 7)
    >>> new_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> test_s
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> new_s is test_s
    True
    >>> double_s = [1, 2, 1, 2, 3, 3]
    >>> double_s = insert_items(double_s, 3, 4)
    >>> double_s
    [1, 2, 1, 2, 3, 4, 3, 4]
    >>> large_s = [1, 4, 8]
    >>> large_s2 = insert_items(large_s, 4, 4)
    >>> large_s2
    [1, 4, 4, 8]
    >>> large_s3 = insert_items(large_s2, 4, 6)
    >>> large_s3
    [1, 4, 6, 4, 6, 8]
    >>> large_s3 is large_s
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while i < len(s) :
        if s[i] == before :
            s.insert(i + 1,after)
            i += 2
        else :
            i += 1
    return s



#this function aims to group s(a list) by fn
def group_by(s, fn):
    """Return a dictionary of lists that together contain the elements of s.
    The key for each list is the value that fn returns when called on any of the
    values of that list.

    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
    """
    grouped = {}
    for e in s :
        key = fn(e)
        if key in grouped:
            grouped[key].append(e)
        else:
            #key已经有了，就直接加进组里。
            #还没有这个key，就新创一个组
            grouped[key] = [e]
    return grouped
    # grouped = {}
    # for e in s:
    #     key = fn(e)
    #     if key in grouped:
    #         grouped[key].append(e)
    #     else:
    #         grouped[key] = e
    # return grouped


def count_occurrences(t, n, x):
    """Return the number of times that x is equal to one of the
    first n elements of iterator t.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(s, 10, 9)
    3
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> count_occurrences(t, 3, 10)
    2
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> count_occurrences(u, 1, 3)  # Only iterate over 3
    1
    >>> count_occurrences(u, 3, 2)  # Only iterate over 2, 2, 2
    3
    >>> list(u)                     # Ensure that the iterator has advanced the right amount
    [1, 2, 1, 4, 4, 5, 5, 5]
    >>> v = iter([4, 1, 6, 6, 7, 7, 6, 6, 2, 2, 2, 5])
    >>> count_occurrences(v, 6, 6)
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for _ in range(n):
        this_one = next(t)
        if this_one == x:
            count += 1
    return count




def repeated(t, k):
    """Return the first value in iterator t that appears k times in a row,
    calling next on t as few times as possible.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> t = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(t, 3)
    8
    >>> u = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(u, 3)
    2
    >>> repeated(u, 3)
    5
    >>> v = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(v, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
# 初始化两个变量，一个用于存储当前元素current_element，
#另一个用于计数count。由于我们在开始时还没有遍历任何元素，可以将current_element初始化为调用next(t)的结果，并将count设为1。
# 进入一个循环，在循环中，我们会尝试不断地从迭代器t中取得下一个元素，同时检查当前元素与上一个是否相同。
# 如果当前元素与上一个元素相同，就将count加一。如果count达到了k，这意味着我们找到了连续出现k次的元素，此时直接返回current_element。
# 如果当前元素与上一个元素不同，就需要重置count为1，并更新current_element为这个新的不同的元素。
# 重复上述步骤，直到找到满足条件的元素。
    last_item = next(t)
    count = 1
    while True:
        current_item = next(t)
        if current_item == last_item:
            count += 1
            if count == k:
                return current_item
        else:
            count = 1
            last_item = current_item

# iterable - version
def repeated_iterable(t,k):
    assert k > 1
    last_item = t[0]
    count = 1
    length = len(t)
    for i in range(1,length):
        current_item = t[i]
        if current_item == last_item:
            count += 1
            if count == k:
                return current_item
        else:
            count = 1
            last_item = current_item
    return None
        

    


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the labels in leaves at each leaf of
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    #只能直接用tree函数，创建一棵树，想要在原来的树的基础上加分支，也只能用tree来加
    #你要加的分支必然是树。（这是树的定义）
    if is_leaf(t):
        return tree(label(t),[tree(leaf) for leaf in leaves])
    else:
        return tree(label(t),[sprout_leaves(s,leaves) for s in branches(t)])


def partial_reverse(s, start):
    """Reverse part of a list in-place, starting with start up to the end of
    the list.

    >>> a = [1, 2, 3, 4, 5, 6, 7]
    >>> partial_reverse(a, 2)
    >>> a
    [1, 2, 7, 6, 5, 4, 3]
    >>> partial_reverse(a, 5)
    >>> a
    [1, 2, 7, 6, 5, 3, 4]
    """
    "*** YOUR CODE HERE ***"
    end = len(s) - 1
    while start < end:
        s[start],s[end] = s[end],s[start]
        start, end = start + 1,end - 1
    





# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

