#A way to do ex 42 with a list
#Still a bit confusing so come back later when know more

# person is-a object
class Person(object):

    def __init__(self, name): #class person has an init that takes self and nam parameter
        self.name = name #person has a name and a pet
        self.pet = None

    def callme(self): #a function that give the name of a person
        return self.name

    def petsyay(self):
        if isinstance(self.pet, list): #checks to see if the pet is in person's pet list.
            namepet = []				#If the pet is in the list, make a list.
            for pet in self.pet:   		#Add the pet's name to this new list
                namepet.append(pet.callpet())
        elif isinstance(self.pet, Pets): 
            namepet = []
            namepet.append(self.pet.callpet())
        else:
            raise ValueError("Not a correct type. Send Pets or list of Pets")
        return namepet


class Pets(object):
    def __init__(self, petname): #pet has a name
        self.petname = petname

    def callpet(self):		#a function that gives you the name of a single pet
        return self.petname


frank = Person("Frank")
poekie = Pets("Poekie")
satan = Pets("Satan")

frank.pet = [poekie, satan]

print frank.petsyay()

frank.pet = poekie
frank.petsyay()
print frank.petsyay()