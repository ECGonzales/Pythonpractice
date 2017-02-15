from sys import exit
class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line		
			
	def lindy(self):						#not correctly working to add to the lyrics
		for line in lyrics:					# try again later??
			if len(lyrics) == 3:
				lyrics.append("5, 6, 7, 8") 
				print lyrics
			else:
				exit[0]
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

#Study drills

lyrics =["Stop in the name of love",
		 "Before you break my heart", 
		 "Baby baby I'm aware of where you go each time you leave my door."]
	 
supremes = Song(lyrics)

#supremes.sing_me_a_song()

#supremes.lindy()


#A Good example https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance
        
        
# Using the customer class
jeff = Customer('Jeff Knupp', 1000.0)

print jeff.withdraw(100.0)


# Another example
class Car(object):

    wheels = 4 #This is valid for all cars => for everything defined in this class

    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    @staticmethod         #Static method that does not need the self
    def make_car_sound():
        print 'VRooooommmm!'
        
	@classmethod         #class method
    def is_motorcycle(cls):
        return cls.wheels == 2

mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4

#for more examples see the rest of this page. They are really good!!!
# Meta class with vehicles example
#left off at Inheritance and the LSP
print Car.wheels
# 4
mustang.make_car_sound() #prints without needing to use the print statment since defined
						# in the def

