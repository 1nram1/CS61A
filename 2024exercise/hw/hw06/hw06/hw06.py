passphrase = "*** PASSPHRASE HERE ***"

def midsem_survey(p):
    """
    You do not need to understand this code.
    >>> midsem_survey(passphrase)
    "3d9f1125b109b311959d068240016badb874603eab75302a445e1a50"
    """
    import hashlib
    return hashlib.sha224(p.encode("utf-8")).hexdigest()


class VendingMachine:
    # add_fund : money to purchase
    # vend:purchase 1 good
    #
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine("candy", 10)
    >>> v.vend()
    "Nothing left to vend. Please restock."
    >>> v.add_funds(15)
    "Nothing left to vend. Please restock. Here is your $15."
    >>> v.restock(2)
    "Current candy stock: 2"
    >>> v.vend()
    "Please add $10 more funds."
    >>> v.add_funds(7)
    "Current balance: $7"
    >>> v.vend()
    "Please add $3 more funds."
    >>> v.add_funds(5)
    "Current balance: $12"
    >>> v.vend()
    "Here is your candy and $2 change."
    >>> v.add_funds(10)
    "Current balance: $10"
    >>> v.vend()
    "Here is your candy."
    >>> v.add_funds(15)
    "Nothing left to vend. Please restock. Here is your $15."

    >>> w = VendingMachine("soda", 2)
    >>> w.restock(3)
    "Current soda stock: 3"
    >>> w.restock(3)
    "Current soda stock: 6"
    >>> w.add_funds(2)
    "Current balance: $2"
    >>> w.vend()
    "Here is your soda."
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, goods,price) -> None:
        self.goods = goods
        self.price = price
        self.current_stock = 0
        self.funds = 0

    def restock(self,number):
        self.current_stock += number
        print(f'"Current {self.goods} stock: {self.current_stock}"')

    def add_funds(self,money):
        if self.current_stock == 0:
            print(f'"Nothing left to vend. Please restock. Here is your ${money}."')
        else:
            self.funds += money
            print(f'"Current balance: ${self.funds}"')

    def vend(self):
        if self.current_stock == 0:
            print('"Nothing left to vend. Please restock."')
            return
        if self.funds == self.price:
            print(f'"Here is your {self.goods}."')
            self.funds = 0
            self.current_stock -= 1

        elif self.funds > self.price:
            print(f'"Here is your candy and ${self.funds - self.price} change."')
            self.funds = 0
            self.current_stock -= 1
        else:
            print(f'"Please add ${self.price - self.funds} more funds."')
        
        



def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    
    """
    "*** YOUR CODE HERE ***"
    # digits = []
    # while n:
    #     digit = n % 10
    #     n = n // 10
    #     digits.append(digit)
    # link = Link.empty
    # for item in digits:
    #     link = Link(item,link)
    # return link
    link = Link.empty
    while n:
        link = Link(n % 10,link)
        n = n // 10
    return link
    

    


def deep_map_mut(func, lnk):
    """Mutates a deep link lnk by replacing each item found with the
    result of calling func on the item. Does NOT create new Links (so
    no use of Link"s constructor).

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if lnk is Link.empty:
        return
    if isinstance(lnk.first,Link):
        deep_map_mut(lnk.first,Link)
    else:
        lnk.first = func(lnk.first)
    deep_map_mut(func,lnk.rest)


def two_list(vals, counts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and counts are the same size. Elements in vals represent the value, and the
    corresponding element in counts represents the number of this value desired in the
    final linked list. Assume all elements in counts are greater than 0. Assume both
    lists have at least one element.
    >>> a = [1, 3]
    >>> b = [1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** YOUR CODE HERE ***"
    vals.reverse()
    counts.reverse()
    times = len(counts)
    link = Link.empty
    for i in range(0,times):
        for _ in range(0,counts[i]):
            link = Link(vals[i],link)
    return link

def two_list_solution(vals,counts):
    def helper(count,index):
        if count == 0:
            if index + 1 == len(vals):
                return Link.empty
            return Link(vals[index + 1], helper(counts[index + 1] - 1, index + 1))
        return Link(vals[index], helper(count - 1,index))
    return helper(counts[0], 0)

def two_list_iterative(vals, counts):
    result = Link(None)
    p = result
    for index in range(len(vals)):
        item = vals[index]
        for _ in range(counts[index]):
            p.rest = Link(item)
            p = p.rest
        return result.rest





class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"

