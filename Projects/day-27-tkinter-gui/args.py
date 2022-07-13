def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)

add(1,2,3)


def mult(**kwargs):
    print(kwargs)

mult(a=1,b=2)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

    
my_car = Car(model="Equinox")
print(my_car.model)