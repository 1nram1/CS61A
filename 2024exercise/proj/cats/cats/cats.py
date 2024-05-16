"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def pick(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns True. If there are fewer than K such paragraphs, return
    the empty string.

    Arguments:
        paragraphs: a list of strings
        select: a function that returns True for paragraphs that can be selected
        k: an integer

    >>> ps = ['hi', 'how are you', 'fine']
    >>> s = lambda p: len(p) <= 4
    >>> pick(ps, s, 0)
    'hi'
    >>> pick(ps, s, 1)
    'fine'
    >>> pick(ps, s, 2)
    ''
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    if k >= len(paragraphs):
        return ''
    
    #其实就算找到第k + 1个满足某个条件的值 ， k从0开始
    #version 1
    # i ,j = 0,0
    # while j <= k:
    #     if i == len(paragraphs):
    #         return ''
    #     if select(paragraphs[i]) :
    #         j += 1
    #     i += 1
    # return paragraphs[i - 1]

    #version 2
    #count 表示目前这个i是第几个满足条件的值
    count = 0
    for i in paragraphs:
        if select(i):
            count += 1
        if count == k + 1 :
            return i
    return ''



    # END PROBLEM 1


def about(subject):
    """Return a select function that returns whether
    a paragraph contains one of the words in SUBJECT.

    Arguments:
        subject: a list of words related to a subject

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> pick(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in subject]), 'subjects should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def about_sth(paragraph):
        #split函数，通过空格把单词与单词分开，才能实现exact match

        target_par = split(lower(remove_punctuation(paragraph)))
        for i in subject:
            if i in target_par:
                return True
        return False
    return about_sth
    


    # END PROBLEM 2


def accuracy(typed, source):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of SOURCE that was typed.

    Arguments:
        typed: a string that may contain typos
        source: a string without errors

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    >>> accuracy('', '')
    100.0
    """
    typed_words = split(typed)
    source_words = split(source)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    #以一个whitespace为一个单位，百分比是你敲对的单位数除以总的单位数决定的
    #以整个单词为一个单位。不是以每一个字母来算你的正确百分比
    #用的是 / float 除法
    #tab don't count as words

    i, j ,count= 0, 0, 0
    length_type = len(typed_words)
    length_source = len(source_words)

    if length_type == 0 and length_source == 0:
        return 100.0
    if length_type ==0 or length_source == 0:
        return 0.0
    while j < length_source and i < length_type :
        if typed_words[i] == source_words[j] :
            count += 1
        i, j = i + 1, j + 1
    return (count / length_type) * 100 





    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string.

    Arguments:
        typed: an entered string
        elapsed: an amount of time in seconds

    >>> wpm('hello friend hello buddy hello', 15)
    24.0
    >>> wpm('0123456789',60)
    2.0
    """
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    # END PROBLEM 4
    length = len(typed) / 5
    spend_time = elapsed / 60
    return length / spend_time




############
# Phase 2A #
############


def autocorrect(typed_word, word_list, diff_function, limit):
    """Returns the element of WORD_LIST that has the smallest difference
    from TYPED_WORD. If multiple words are tied for the smallest difference,
    return the one that appears closest to the front of WORD_LIST. If the
    difference is greater than LIMIT, instead return TYPED_WORD.

    Arguments:
        typed_word: a string representing a word that may contain typos
        word_list: a list of strings representing source words
        diff_function: a function quantifying the difference between two words
        limit: a number

    >>> ten_diff = lambda w1, w2, limit: 10 # Always returns 10
    >>> autocorrect("hwllo", ["butter", "hello", "potato"], ten_diff, 20)
    'butter'
    >>> first_diff = lambda w1, w2, limit: (1 if w1[0] != w2[0] else 0) # Checks for matching first char
    >>> autocorrect("tosting", ["testing", "asking", "fasting"], first_diff, 10)
    'testing'
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if typed_word in word_list :
        return typed_word
    min_diff_word = typed_word
    min_diff = limit + 1
    for word in word_list:
        this_diff = diff_function(typed_word,word,limit)
        if this_diff < min_diff:
            min_diff = this_diff
            min_diff_word = word
    if min_diff > limit :
        return typed_word
    return min_diff_word
    #alternative:
    if typed_word in word_list:
        return typed_word
    word = min(word_list,key = lambda word: diff_function(typed_word,word,limit))
    min_diff = diff_function(typed_word,word,limit)
    if min_diff <= limit:
        return word
    return typed_word
    


    # END PROBLEM 5


def feline_fixes(typed, source, limit):
    """A diff function for autocorrect that determines how many letters
    in TYPED need to be substituted to create SOURCE, then adds the difference in
    their lengths and returns the result.

    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_fixes("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_fixes("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_fixes("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_fixes("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_fixes("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6

    # diff_now 
    # if a > limit:
    #     return a
    length_diff = abs(len(typed) - len(source))
    if length_diff > limit :
        return limit + 1
    
    def feline_fix_helper(type,source,diff_now):
        if diff_now + length_diff > limit:
            return limit + 1
        if len(type) > 0 and len(source) > 0:
            if type[0] == source[0]:
                return feline_fix_helper(type[1:],source[1:],diff_now)
            return feline_fix_helper(type[1:],source[1:],diff_now + 1)
        return diff_now + length_diff
    return feline_fix_helper(typed,source,0)    

    # END PROBLEM 6


############
# Phase 2B #
############


# 该函数是计算两个字符串之间编辑距离的算法（例如Levenshtein距离），
# 这个函数计算出的应该是最小的编辑次数。
# 编辑距离的算法工作方式是，它会考虑所有可能的编辑操作序列，
# 然后找出将一个字符串转换成另一个字符串所需的最少操作数。
# 在遍历了所有可能的操作序列后，它会产生一个最小的编辑次数，
# 这是将一个字符串转换为另一个字符串所需的最小单字符编辑（插入、删除或替换）次数。如果算法实现得当，那么它就能够确保找到最优解。
# 请注意，算法的效率很大程度上取决于它是如何实现的。
# 未经优化的递归解法可能会重复计算许多子问题，从而导致效率低下。
# 动态规划方法通过存储中间结果来避免重复计算，通常可以提高效率。
# 如果实现了这些优化措施，算法就能够在合理的时间内求出最小编辑距离。



def minimum_mewtations(typed, source, limit):
    """A diff function that computes the edit distance from TYPED to SOURCE.
    This function takes in a string TYPED, a string SOURCE, and a number LIMIT.
    Arguments:
        typed: a starting word
        source: a string representing a desired goal word
        limit: a number representing an upper bound on the number of edits
    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """ 
    #不一定要用helper_function。用helper function 主要就是因为要记录已经有多少不同了（已进行几次edit）
    #注意： 或者最多还剩多少可以不同（还可以edit几次）。所以直接用参数limit来反映edit次数（还剩几次）
    #另外，注意题目让你简化的时操作次数，并不是返回值必须是离limit很近


    #base case
    if  len(typed) == 0 or len(source) == 0 : # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(typed) + len(source)
        # END



    # Recursive cases should go below here
    if typed[0] == source[0] : 
        # BEGIN
        "*** YOUR CODE HERE ***"
        return minimum_mewtations(typed[1:],source[1:],limit)
        # END
    else:

        #note: 强调过很多次，写递归时，不要去想着写出能一次找出最优解的写法。
        #写递归无法写成最优解
        #永远记住：递归只是 暴力解法。他是帮你遍历所有情况（难以想象的多的情况）
        #真的是完完全全的所有情况，去看哪个是个解。所以才是指数增长。记住了，所有情况！
        #写的时候要去想，我的代码如何才能写成遍历了所有情况的
        #而不是去想如何直接找到最优解，不去管别的情况
        #所以递归会遍历到很多，多余，一眼就不可能成功的情况
        #牢记：调用递归时，默认这个函数功能已经得到实现。比较容易去思考该怎么写
        #比如这个调用 minimum_mewtations(type.source,limit),我们就要想成，他会返回从type到source
        #的“最小编辑次数”

        #note:递归还有一个层次的问题，要注意 应该在哪个层次思考这个问题



        #编辑次数到头，还没完全相等，这种情况已经不是答案了。return 1 ，经过
        #递归返回值相加后。  最终返回值就变成 1 + limit了
        if limit == 0:
            return 1


        # 第一个字符不相等，我们有三种处理的办法（已经是所有的办法了）

        #这是逻辑上的 add ,remove substitute

        add = 1 + minimum_mewtations(typed,source[1:],limit - 1) 
        remove = 1 + minimum_mewtations(typed[1:],source,limit - 1)
        substitute = 1 + minimum_mewtations(typed[1:],source[1:],limit - 1)

        # 计算最小值：最后一步是比较这三种编辑操作产生的编辑距离，并返回最小值，
        # 这就是完成一个编辑操作后所需要的最小编辑次数。
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add,remove,substitute)
        # END

   

    #下面你自己写的代码，尝试去判断什么情况该执行add，什么情况执行remove，substitute。
    #这种想法不应该出现在递归里面，我说了:递归就是要遍历所有清空，他不去找最优解
    #就是纯纯的把每种情况都看一遍。



    # def mininum_helper(typed,source,diff_now) :
    #     length = abs(len(source) - len(typed))
    #     if diff_now + length > limit :
    #         return limit + 1    
    #     if typed[0] != source[0] and len(typed) > len(source) :
    #         return minimum_mewtations(source[0] + typed,source,diff_now + 1)
    #     elif typed[0] != source[0]:
    #         typed[0] = source[0]
    #         return minimum_mewtations(typed,source,diff_now + 1)
    #     else :
    #         return minimum_mewtations(typed,source,diff_now)
    









def final_diff(typed, source, limit):

    """A diff function that takes in a string TYPED, a string SOURCE, and a number LIMIT.
    If you implement this function, it will be used."""

    FINAL_DIFF_LIMIT = 6 # REPLACE THIS WITH YOUR LIMIT
        #base case
    if  len(typed) == 0 or len(source) == 0 : # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(typed) + len(source)
        # END



    # Recursive cases should go below here
    if typed[0] == source[0] : 
        # BEGIN
        "*** YOUR CODE HERE ***"
        return minimum_mewtations(typed[1:],source[1:],limit)
        # END
    else:

        #note: 强调过很多次，写递归时，不要去想着写出能一次找出最优解的写法。
        #写递归无法写成最优解
        #永远记住：递归只是 暴力解法。他是帮你遍历所有情况（难以想象的多的情况）
        #真的是完完全全的所有情况，去看哪个是个解。所以才是指数增长。记住了，所有情况！
        #写的时候要去想，我的代码如何才能写成遍历了所有情况的
        #而不是去想如何直接找到最优解，不去管别的情况
        #所以递归会遍历到很多，多余，一眼就不可能成功的情况
        #牢记：调用递归时，默认这个函数功能已经得到实现。比较容易去思考该怎么写
        #比如这个调用 minimum_mewtations(type.source,limit),我们就要想成，他会返回从type到source
        #的“最小编辑次数”

        #note:递归还有一个层次的问题，要注意 应该在哪个层次思考这个问题



        #编辑次数到头，还没完全相等，这种情况已经不是答案了。return 1 ，经过
        #递归返回值相加后。  最终返回值就变成 1 + limit了
        if limit == 0:
            return 1


        # 第一个字符不相等，我们有三种处理的办法（已经是所有的办法了）

        #这是逻辑上的 add ,remove substitute

        add = 1 + minimum_mewtations(typed,source[1:],limit - 1) 
        remove = 1 + minimum_mewtations(typed[1:],source,limit - 1)
        substitute = 1 + minimum_mewtations(typed[1:],source[1:],limit - 1)

        # 计算最小值：最后一步是比较这三种编辑操作产生的编辑距离，并返回最小值，
        # 这就是完成一个编辑操作后所需要的最小编辑次数。
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add,remove,substitute)
        # END


###########
# Phase 3 #
###########


def report_progress(typed, source, user_id, upload):
    """Upload a report of your id and progress so far to the multiplayer server.
    Returns the progress so far.

    Arguments:
        typed: a list of the words typed so far
        source: a list of the words in the typing source
        user_id: a number representing the id of the current user
        upload: a function used to upload progress to the multiplayer server

    >>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
    >>> # The above function displays progress in the format ID: __, Progress: __
    >>> print_progress({'id': 1, 'progress': 0.6})
    ID: 1 Progress: 0.6
    >>> typed = ['how', 'are', 'you']
    >>> source = ['how', 'are', 'you', 'doing', 'today']
    >>> report_progress(typed, source, 2, print_progress)
    ID: 2 Progress: 0.6
    0.6
    >>> report_progress(['how', 'aree'], source, 3, print_progress)
    ID: 3 Progress: 0.2
    0.2
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    i = 0
    count = 0
    while i < len(typed):
        if typed[i] != source[i]:
            break
        i += 1
        count += 1
    ratio = count / len(source)
    upload({'id': user_id, 'progress': ratio})
    return ratio
        

    # END PROBLEM 8


def time_per_word(words, timestamps_per_player):
    """Given timing data, return a match data abstraction, which contains a
    list of words and the amount of time each player took to type each word.

    Arguments:
        words: a list of words, in the order they are typed.
        timestamps_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.

    >>> p = [[75, 81, 84, 90, 92], [19, 29, 35, 36, 38]]
    >>> match = time_per_word(['collar', 'plush', 'blush', 'repute'], p)
    >>> get_all_words(match)
    ['collar', 'plush', 'blush', 'repute']
    >>> get_all_times(match)
    [[6, 3, 6, 2], [10, 6, 1, 2]]
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    
    length = len(timestamps_per_player)
    times = []
    for i in  range(length) :
        size = len(timestamps_per_player[i])
        for j in range(size - 1):
            timestamps_per_player[i][j] = timestamps_per_player[i][j + 1] - timestamps_per_player[i][j]
        times.append(timestamps_per_player[i][:-1])

    return match(words,times)



    # END PROBLEM 9


def fastest_words(match):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        match: a match data abstraction as returned by time_per_word.

    >>> p0 = [5, 1, 3]
    >>> p1 = [4, 1, 6]
    >>> fastest_words(match(['Just', 'have', 'fun'], [p0, p1]))
    [['have', 'fun'], ['Just']]
    >>> p0  # input lists should not be mutated
    [5, 1, 3]
    >>> p1
    [4, 1, 6]
    """
    player_indices = range(len(get_all_times(match)))  # contains an *index* for each player
    word_indices = range(len(get_all_words(match)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    res = []
    for _ in player_indices:
        res.append([])
    for i in word_indices:
        #player_fast = min(player_indices,key=time(,i,match))
        min_time = time(match,0,i)
        #min_player = 0
        for j in player_indices:
            if time(match,j,i) < min_time and j != 0:
                min_time = time(match,j,i)
                min_player = j
        word = get_word(match,i)
        res[min_player].append(word)
    return res


            
        






    # END PROBLEM 10


def match(words, times):
    """A data abstraction containing all words typed and their times.

    Arguments:
        words: A list of strings, each string representing a word typed.
        times: A list of lists for how long it took for each player to type
            each word.
            times[i][j] = time it took for player i to type words[j].

    Example input:
        words: ['Hello', 'world']
        times: [[5, 1], [4, 2]]
    """
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return {"words": words, "times": times}


def get_word(match, word_index):
    """A utility function that gets the word with index word_index"""
    assert 0 <= word_index < len(get_all_words(match)), "word_index out of range of words"
    return get_all_words(match)[word_index]


def time(match, player_num, word_index):
    """A utility function for the time it took player_num to type the word at word_index"""
    assert word_index < len(get_all_words(match)), "word_index out of range of words"
    assert player_num < len(get_all_times(match)), "player_num out of range of players"
    return get_all_times(match)[player_num][word_index]

def get_all_words(match):
    """A selector function for all the words in the match"""
    return match["words"]

def get_all_times(match):
    """A selector function for all typing times for all players"""
    return match["times"]


def match_string(match):
    """A helper function that takes in a match data abstraction and returns a string representation of it"""
    return f"match({get_all_words(match)}, {get_all_times(match)})"

enable_multiplayer = False  # Change to True when you're ready to race.

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        source = pick(paragraphs, select, i)
        if not source:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(source)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, source))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)