def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

#note: four important quetions about resursive
# What recursive calls will you make?
# What type of values do they return?
# What do the possible return values mean?
# How can you use those return values to complete your implementation?






def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    "*** YOUR CODE HERE ***"

    #base case 1
    #whether p is a list of length one with the label of t as its only element.

    # alternative : len(p) == 1 and p[0] == label(t)

    if p == [label(t)]:
        return True
    

    #The second base case should check if the first element of p matches the label of t
    elif label(t) != p[0]:
        return False
    

    else:
        #wrong version
        # for branch in branches(t) :
        #     return has_path(branch,p[1:]) 

        #Note:不知道如何处理，tree-decision里面有一个true就行，其他全是False也无所谓
        #感觉cpp中可以用 左孩子 || 右孩子，这里孩子貌似有点多



    #right version

    #利用 for-loop 把return False放在for loop 外面 
    #这样就解决了上面说的问题：
    #tree-decision里面有一个true，整体就为True，其他全是False也无所谓


        for branch in branches(t):
            if has_path(branch,p[1:]):
                return True
            
        #每一个child那都走不通，才return False
        return False
    


    #上面是较为通用的语法，下面展示pythonic的办法
    # any(...): 这个函数用来检查给定的迭代器中是否至少有一个元素为真。
    # 如果列表中至少有一个 has_path(b, p[1:]) 的结果是 True，any 函数就会返回 True；
    # 否则，如果没有任何符合条件的路径，它返回 False。

    #return any([has_path(b, p[1:]) for b in branches(t)])
    
    


def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
#Note: 首先我们每次进入find_path，应该判断这个根结点的label是不是x
#然后需要一个变量去记录我们走过的路径，或者用别的方式记录我们走过的路径
#recursive case : 每个child都要去递归调用，递归调用时x不变，t变就行了
#只要能找到一条路径就行（也只有一条路径）
#个人感觉;写个helper_function ，多一个变量去记录路径.最终尝试失败

    #base case
    if label(t) == x:
        return [label(t)]
    

    for b in branches(t) :
        path = find_path(b,x)
        if path:
            return [label(t)] + path
    #当遇到一条path可信时,path就会不断加[t],一层一层地加上去了

    #以目前这个t为根节点的路径，一条也没找到，返回None,
    #感觉有点类似与False
    return None   



   
def find_path_own(t,x):
    #写递归函数的技巧，写之前，描述清楚这个函数的功能，因为之后递归调用这个函数时，就默认这个功能成立，去想怎么递归调用比较容易
    """if find a path to x,return the path which is represented as a list of label
       return None otherwise
    """
    if label(t) == x:
        return [label(t)]
    #一次没找到不代表这条路就不是答案，不能直接return False

    #根节点不是目标x，那就遍历这个根的所有child
    for b in branches(t):
        path = find_path_own(b,x)
        if path:
            return [label(t)] + path
    return None
        


# !!! important  for-loop 搭配 if   
#可以实现递归中，所有explore的可能性中只要有一种满足条件就可以的情形
#如果所有可能性中有满足条件的情况，会在for循环里return，结束函数。一个都不满足，就会退出for循环后，return None/False之类的
# for i in all-possibilities:
#      ...
#     if (the result of recursive call)：
#          return (some process of (the result of recursive call))
# return None/False ...