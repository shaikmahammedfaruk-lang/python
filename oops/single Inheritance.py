class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):   # single
    def speak(self):
        return "woof"
a1=Animal() 
a2=Dog()  
print(a1.speak()) 
print(a2.speak())