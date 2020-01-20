# coroutines
def grep1(pattern):
    print('start grep')
    while True:
        line = yield
        if pattern in line:
            print(line)


def grep2(pattern):
    print('start grep')
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('stop grep')


def grep_python_coroutine():
    g = grep1('python')
    next(g)
    g.send('python is the best!')
    g.close()


print('Example 1')
g = grep1('python')
next(g)
g.send('golang is better?')
g.send('python is simple!')
print()

print('Example 2')
g = grep2('python')
next(g)
g.send('golang is better?')
g.send('python is simple!')
print()

print('Example 3')
g = grep2('python')
next(g)
g.send('golang is better?')
# g.throw(RuntimeError, 'something wrong')
print()

print('Example 4')
# PEP 380
g = grep_python_coroutine()
print(g)
print()


def grep_python_coroutine():
    g = grep1('python')
    yield from g


print('Example 5')
# PEP 380
g = grep_python_coroutine()
print(g)
g.send(None)
g.send('python wow!')
print()

print('Example 6')


def chain(xiterable, yiterable):
    yield from xiterable
    yield from yiterable


def the_same_chain(xiterable, yiterable):
    for x in xiterable:
        yield x

    for y in yiterable:
        yield y


a = [1, 2, 3, 4]
b = (7, 15)
for x in chain(a, b):
    print(x, end=' ')
print()
