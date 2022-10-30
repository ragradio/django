class A():
    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 de A")


class B(A):
    def __init__(self):
        self.__y = 1

    def m1(self):
        print("m1 de B")

c = B()
c.m1()

class ClassA:
    def message(self):
        print("Hola")

class ClassB(ClassA):
    def message(self):
        super().message()
        print("mundo!")

b = ClassB()
b.message()


