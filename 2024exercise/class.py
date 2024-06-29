class food:
    def __init__(self,catagory,name) :
        self._calories = 10
        self._catagory = catagory
        self._name = name


class Animal:
    species_name = "Animal"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self,name,age = 0) :
        self.name = name
        self.age = age
        self.calorie_eaten = 0
        self.happiness = 0
    def play(self,num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("play time")
    
    def eat(self,food) :
        self.calorie_eaten += food.calories
        print(f"yommy {food.name}")
    
class Panda(Animal):
    species_name = "Panda"
    play_multiplier = 4
    interact_increment = 1
    def eat(self,food):
        if food._name == "bamboo" :
            self.calorie_eaten += food._calories
            self.happiness += 1
            print("great bamboo")
        else :
            self.happiness -= 1
        
bamboo = food("veget","bamboo")
Panda_1 = Panda("sjm",18)
Panda_1.eat(bamboo)
print(Panda_1.happiness)
print(Panda_1.calorie_eaten)

def tree(label,branches = []):
    return [label] + list(btanches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)


class Tree :
    def __init__(self,label,branches = []) :
        self.label = label
        for branch in branches:
            assert isinstance(brance, Tree)
        self.branches = list(branches)
        # list() just make sure branches is a list

    def is_leaf(self):
        return not self.branches
    
    def __str__(self) :
        return '\n'.joinI(self.indented())

    def __repr__(self):
        if self.branches:
            branch_str = ',' + repr(self.branches)
        else:
            branch_str =''
        return 'Tree({0}{1})'.format(self.label,branch_str)
    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append(' ' + line)
        return [str(self.label)] + lines
    
class Link:
    empty = ()

    def __init__(self,first,rest = empty) -> None:
        assert rest is Link.empty or isinstance(rest,Link)
        self.first = first
        self.rest = rest

    def __repr__(self) -> str:
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr =''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self) -> str:
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def range_link(start, end):
    """
    >>> range_link(3,6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start,range_link(start + 1,end))
    

def map_link(f,LinkList):
    if LinkList is Link.empty:
        return Link.empty
    return Link(f(LinkList.first),map_link(f,LinkList.rest))

def filter_link(f,ll):
    if ll is Link.empty:
        return Link.empty
    if f(ll.first):
        return Link(ll.first,filter_link(f,ll.rest))
    else:
        return filter_link(f.ll.rest)

def insert_front(link_list,new_val):
    return Link(new_val,link_list)

def add(ordered_list,new_val):
    if new_val < ordered_list.first:
        original_first = ordered_list.first
        ordered_list.first = new_val
        ordered_list.rest = Link(original_first,ordered_list.rest)
    elif new_val > ordered_list.first and ordered_list.rest is Link.empty :
        ordered_list.rest = Link(new_val)
    elif new_val > ordered_list.first:
        add(ordered_list.rest,new_val)
    return ordered_list


        

