class LivingThing:
    pass

class Plant(LivingThing):
    pass

class Flower(Plant):
    def name(self):
        return "rose"
c1 = Flower()
print(c1.name())    