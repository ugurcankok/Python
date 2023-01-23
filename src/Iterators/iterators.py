# iterable: An object that can be generated as an iterable object in Python is called an iterable object.
# iterator: Iterators is an object that gives Python the ability to iterate.

class Counter:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


for i in Counter(10, 20):
    print(i)
