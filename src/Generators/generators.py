# generator: It is a function that creates an iterable object.
# They do not take up memory space, so they work seamlessly on large data.

import sys

my_list = [i * 2 for i in range(10000)]
print(sys.getsizeof(my_list))

gen = (i ** 2 for i in range(10000)) # generator comprehension
print(sys.getsizeof(gen))


def fib_gen(max_num):
    a, b = 0, 1
    count = 0

    while count < max_num:
        a, b = b, a + b
        yield b
        count += 1


for i in fib_gen(10000000):
    print(i)
