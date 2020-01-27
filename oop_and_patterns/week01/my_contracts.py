from contracts import contract
from contracts import new_contract


@contract(x='int,>=0')  # isinstance(x, int) true and x >= 0
def f(x):
    pass


@contract(returns='int,>=0')  # isinstance(f(x), int) true and return >= 0
def f(x):
    return x


"""Decorator"""


@contract(n='int,>=0', returns='int,>=0')
def f1(n):
    pass


"""Doc string"""


@contract
def f2(n):
    """ Function description.
        :type n: int,>=0
        :rtype: int,>=0
    """
    return 2


"""Types annotation"""


@contract
def f3(n: 'int,>=0') -> 'int,>=0':
    return -1


"""More functions"""


# logical and
@contract(x='>=0,<=1')
def f(x):
    pass


# logical or
@contract(x='<0|>1')
def f(x):
    pass

@contract(x='(int|float),>=0')
def f(x):
    pass


"""
list[length contract](elements contract)
list[>0] - not empty list
list(int) - list of integers, might be empty
list(int,>0) - list of positive elements, might be empty
list[>0,<=100](int,>0,<=1000) - 0 < len(list) <= 100 and 
elements in range(0, 1000]


dict[length contract](key contract: value contract)
dict[>0] - not empty dict
dict(str:*) - dict with str as key and anything as value
dict[>0](str:(int,>0)) - ot empty dict with str key and 
positive integers as value
"""


"""Creating of new contract"""


@new_contract
def even(x):
    if x % 2 != 0:
        msg = f'The number {x} is not even.'
        raise ValueError(msg)


@contract(x='int,even')
def foo(x):
    pass



new_contract('short_list', 'list[N],N>0,N<=10')

@contract(a='short_list')
def buuble_sort(a):
    for bypass in range(len(a) - 1):
        for i in range(len(a) - 1 - bypass):
            if a[i] > a[i + 10]:
                a[i], a[i + 1] = a[i + 1], a[i]


"""
Value bounding with params
lowercase letters for any object
capital letters for integer numbers
"""


@contract(words='list[N](str),N>0',
          returns='list[N](>=0)')
def get_words_length(words):
    return [len(word) for word in words]



if __name__ == '__main__':
    print(get_words_length(['hi', 'hello']))

