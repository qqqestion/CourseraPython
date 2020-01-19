def even_range(start, end):
    current = start if start % 2 == 0 else start + 1
    while current < end:
        yield current
        current += 2


for even in even_range(0, 10):
    print(even, end=' ')
print()
for even in even_range(1, 10):
    print(even, end=' ')
print()

my_range = even_range(0, 4)
print(next(my_range))
print(next(my_range))
try:
    print(next(my_range))
except StopIteration:
    print('range is up')


def list_generator(list_obj):
    for item in list_obj:
        print('After yielding {}'.format(item))
        yield item


generator = list_generator([1, 2])
print(next(generator))
print(next(generator))


def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a
        a, b = b, a + b


print('Fibonacci')
for num in fibonacci(5):
    print(num, end=' ')
print()


def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
        if not value:
            break
        total += value


generator = accumulator()
# accumulating its value just awesome!!!
print('Accumulator')
print(next(generator))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
