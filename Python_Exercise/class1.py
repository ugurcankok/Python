
class First:
    a=int(input("Enter your first number:"))
    b=int(input("Enter your second number:"))
    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a-self.b


print(First().sum())
print(First().sub())

class Second:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def topla(self):
        return self.x+self.y

t=int(input("Enter number:"))
y=int(input("Enter number:"))
print(Second(t,y).topla())