class Dog:

    def __init__(self, name, breed): #initialization of the class
        self.name = name
        self.breed = breed

    def bark(self):
        print("bark")

    def giveMeAttributes(self):
        print(self.name)
        print(self.breed)
dog_1=Dog("Firulais", "Chihuahua")
dog_2=Dog("bittyBit","Yorkie")
print(dog_1)
dog_1.bark()
dog_1.giveMeAttributes()
dog_2.giveMeAttributes()