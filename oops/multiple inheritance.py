class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck(Flyer, Swimmer): 
    pass
c1=Duck()
print(c1.swim())
print(c1.fly())
