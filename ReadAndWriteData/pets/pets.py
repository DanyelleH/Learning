import json
class DuplicateNameError(Exception):
    pass
class NonExistentPet(Exception):
    pass
class NeighborhoodPets:
    def __init__(self):
        self._allPets={} #create dictionary to hold all owners/pets

    def add_pet(self, pet_name, species, owners_name):
        if pet_name in self._allPets:
            raise DuplicateNameError(" Pet name already exists in the neighborhood")
        else:
            self._allPets[pet_name]= {
                "species": species,
                "Owner" : owners_name
            }

    def remove_pet(self, pet_name):
        if pet_name in self._allPets:
            del self._allPets[pet_name]
        else:
            raise NonExistentPet("Pet does not exist")
        
    def get_owner(self, pet_name):
        if pet_name in self._allPets:
            return self._allPets[pet_name]["Owner"]
        else:
            raise NonExistentPet(" Pet Does Not Exist")
        
    def save_to_json(self, file_name):
        with open(f"/Users/danyelleridley/Documents/Learning/ReadAndWriteData/pets/{file_name}.json", 'w') as outfile:
            json.dump(self._allPets, outfile)# dump what where

    def read_json(self, file_name):
        with open(file_name,'r') as infile:# overwrites allPets
            self._allPets = json.load(infile)
            print(self._allPets)

    def get_species_list(self):
        all_species = []
        for pets in self._allPets.values():
            all_species.append(pets["species"])
        return set(all_species)


np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')

np.save_to_json("pets.json")
# np.remove_pet("Tiny")
spot_owner = np.get_owner("Spot")
# print(spot_owner)
species_set = np.get_species_list()
print(species_set)