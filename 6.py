class Greetings():
    def Hello(self,name=None,age=None):
        if name is None and age is None:
            print("Hello")
        elif name is not  None and age is None:
            print(f"Hello {name}")
        elif name is not None and age is not None:
            print(f"Hello {name} with {age}age")
greet=Greetings()
greet.Hello()
greet.Hello("Ava")
greet.Hello("Ava",26)


class findArea():
    def area(self,a=None,b=None):
        if a is  None and b is None:
            print("0")
        elif a is not None and b is None:
            print("area of square is",a*a)
        elif a is not None and b is not None:
            print("area of rectangle",a*b)
Ar=findArea()
Ar.area()
Ar.area(10)
Ar.area(10,5)