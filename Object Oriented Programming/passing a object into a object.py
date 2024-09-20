class Pet:

    def __init__(self, name):
        self._name = name
    
    def __str__(self): ## thunder method for string
        return self._name

    def get_name(self): #getter method
        return self._name
    
class Home:
    def __init__(self, owner):
        self._owner = owner
        self._pets = [] # default that comes with a home.
    
    def __str__(self):
        return self._owner

    def adopt_pet(self, pet_object):
        self._pets.append(pet_object)

    def show_pets(self):
        return self._pets

pet_1 = Pet("Alfred")
my_home = Home("Danyelle")

print(pet_1, my_home)
print(my_home.show_pets())
my_home.adopt_pet(pet_1)

## if you call show pets without the loop, its not going to return every object in the home object.
for pet in my_home.show_pets():
    print(pet)