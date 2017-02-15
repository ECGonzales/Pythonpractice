## Animal is-a object (yes sort of confusing) look at the extra credit
# Making edits based on this code for number 3.
#http://codepad.org/lxFV13jw
class Animal(object):
	
	voice = " I am an animal and thus I do not speak."
	
	def __init__(self, name):
		self.name = name # Animal has a name
		
	def talk(self): # a function named talk that takes self parameters => ***.talk() 
		print Animal.voice #This makes your animal say voice.
	
## -- Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## -- dog has-a name
		self.name = name
		
	def speak(self, attr): #A function that lets the do speak need to tell it what to say.
		Dog.voice = attr   # by entering name.speak("what to say")
		print attr
		

		
## -- cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## -- cat has-a name
		self.name = name
		
## -- person is-a object
class Person(object):

	words = "We are people, and therefore can speak."

	def __init__(self, name):
		## -- person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None
		
	def talk(self):
		print Person.words
		
## -- Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## A way to run the __init__ method of the parent class (here person) reliably
		## still fairly confusing :(
		super(Employee, self).__init__(name)
		## -- employee has-a salary
		self.salary = salary
		
	def make_money(self, mood):
		Employee.mood = mood
		print "Today I am feeling %s about making money!" % mood
		
## --- Fish is-a object
class Fish(object):
	pass
	
## -- Salmon is-a fish
class Salmon(Fish):
	pass

## -- Halibut is-a fish
class Halibut(Fish):
	pass
	
	
## rover is-a Dog
rover = Dog("Rover")

## -- Satan is a cat
satan = Cat("Satan")

## -- Mary is-a person
mary = Person("Mary")

## -- Mary has-a pet Satan who is-a cat
mary.pet = satan

## -- Frank is-a employee who has-a salary
frank = Employee("Frank", 120000)

## -- Frank has-a pet, Rover who is-a dog
frank.pet = rover

## -- flipper is-a fish
flipper = Fish()

## -- crouse is-a Salmon, which is-a fish
crouse = Salmon()

## -- harry is a halibut, which is-a fish
harry = Halibut()

rover.talk()
rover.speak("woof woof")

frank.talk()
print "Hi I am Frank"
print "How is frank feeling today?"
feeling = raw_input("> ")
frank.make_money(feeling)