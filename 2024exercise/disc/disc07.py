def draw(hand, position):
    """
    >>> hand = ['A', 'k', 'Q', 'J', 10, 9]
    >>> draw(hand,[2, 1, 4])
    ['k', 'Q', 10]
    >>> hand
    ['A', 'J', 9]
    """

    return list(reversed([hand.pop(p) for p in reversed(sorted(position))]))



LOWERCASE_LETTERS = 'abdcdefghijklmnopqrstuvwxyz'

class CapsLock:
    def __init__(self) -> None:
        self.pressed = 0
    
    def press(self):
        self.pressed += 1

class Button:
    caps_lock = CapsLock()

    def __init__(self,letter,output) -> None:
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0

    def press(self):
        self.pressed += 1
        "Your code here"
        if Button.caps_lock.pressed % 2 == 0:
            self.output(self.letter)
        else:
            self.output(self.letter.upper())
        return self
    

class KeyBoard:
    def __init__(self) -> None:
        self.typed = []
        self.keys = {letter : Button(letter,self.typed.append) for letter in LOWERCASE_LETTERS}

    def type(self,word):
        assert all([w in LOWERCASE_LETTERS for w in word])
        for w in word:
            self.keys[w].press()
            

            
#Question_3


class Eye:
    """An eye.

    >>> Eye().draw()
    '•'
    >>> print(Eye(False).draw(), Eye(True).draw())
    • -
    """
    def __init__(self, closed=False):
        self.closed = closed

    def draw(self):
        if self.closed:
            return '-'
        else:
            return '•'

class Bear:
    """A bear.

    >>> Bear().print()
    ʕ •ᴥ•ʔ
    """
    def __init__(self):
        self.nose_and_mouth = 'ᴥ'

    def next_eye(self):
        return Eye()

    def print(self):
        left, right = self.next_eye(), self.next_eye()
        print('ʕ ' + left.draw() + self.nose_and_mouth + right.draw() + 'ʔ')


class SleepyBear(Bear):
    """A bear with closed eyes.

    >>> SleepyBear().print()
    ʕ -ᴥ-ʔ
    """
    def next_eye(self):
        return Eye(True)                
            

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ʕ -ᴥ•ʔ
    """
    def __init__(self):
        super().__init__()
        self.eye_calls = 0
        

    def next_eye(self):
        self.eye_calls += 1
        return Eye(self.eye_calls % 2 )
        
