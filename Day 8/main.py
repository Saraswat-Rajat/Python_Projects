# functions with inputs

import math


def greet():
    print("hi")
    print("hello")
    print("bye")


greet()


def add(a, b):
    sum = a+b
    print(sum)


add(2, 4)


def greet_with(name, location):
    print(f"Hello {name}, What it is like in {location}")


greet_with("rajat", "lucknow")


greet_with(location="patna", name="pogo")


def area(l, h, cov):
    cans = math.ceil(l*h/cov)
    print(cans)


area(l=90, h=78, cov=12)
