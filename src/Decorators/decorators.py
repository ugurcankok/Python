def hello(fn):
    def wrapper(ad):
        print("welcome")
        fn(ad)
        print("see you around")

    return wrapper

@hello
def good_morning(ad):
    print("good morning, my name is " + ad)

@hello
def have_a_nice_day(ad):
    print("good morning, my name is" + ad)


good_morning("ugur")
have_a_nice_day("can")