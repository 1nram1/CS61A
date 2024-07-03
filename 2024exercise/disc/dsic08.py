class Link:
    """A linked list is either a Link object or Link.empty

    >>> s = Link(3, Link(4, Link(5)))
    >>> s.rest
    Link(4, Link(5))
    >>> s.rest.rest.rest is Link.empty
    True
    >>> s.rest.first * 2
    8
    >>> print(s)
    <3 4 5>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    

def strange_loop():
    result = Link(6,Link(Link(1)))
    result.rest.first.rest = result
    return result

def sum_rec(s):
    if s is Link.empty:
        return 0
    return s.first + sum_rec(s.rest)
    


def sum_iter(s):
    total = 0
    while s is not Link.empty:
        total += s.first
        s = s.rest
    return total

def Overlap(s,t):
    count = 0
    while s is not Link.empty and t is not Link.empty :
        if s.first < t.first:
            s = s.rest
        elif s.first > t.first:
            t = t.rest
        else:
            t = t.rest
            s = s.rest
            count += 1
    # if s is Link.empty:
    #     while t is not Link.empty:
    #         count += 1
    #         t = t.rest
    # else:
    #     while s is not Link.empty:
    #         count += 1
    #         s = s.rest
    return count

def Overlap_recursive(s,t):
    if s is Link.empty or t is Link.empty:
        return 0
    if s.first == t.first:
        return Overlap_recursive(s.rest,t.rest) + 1
    elif s.first < t.first:
        return Overlap_recursive(s.rest,t)
    elif s.first > t.first:
        return Overlap_recursive(s,t.rest)




def length(s):
    if s is Link.empty:
        return 0
    else:
        return 1 + length(s.rest)

def filter_link(f, s):
    """ Return s(linklist) 满足 f 的元素组成的list"""
    if s is Link.empty:
        return s
    else:
        frest = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, frest)
        else:
            return frest

def contained_in(s):
    """Return True if s(linklist) contains x, False otherwise"""
    def f(s, x):
        if s is Link.empty:
            return False
        else:
            return s.first == x or f(s.rest, x)
    return lambda x: f(s, x)



def overlap(s, t):
    """For s and t with no repeats, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8, Link(12))))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b.rest)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    return length(filter_link(contained_in(t), s))


def divide(n, d):
    assert n > 0 and n < d
    cache = {}
    result = Link(0)
    tail = result
    while n not in cache:
        q, r = 10 * n // d, 10 * n % d
        tail.rest = Link(q)
        tail = tail.rest
        cache[n] = tail
        n = r
    tail.rest = cache[n]
    return result






def display(s, k = 10):
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        digits += str(s.first)
        s = s.rest
    print(digits + '...')