#Inheritance examples
#******* A) Implicit Inheritance *********
#class Parent(object):

#	def implicit(self):
#		print "parent implicit()"
		
#class Child(Parent):
#	pass  #<- here child has no attributes different from the parent

#dad = Parent()
#son = Child()

#dad.implicit()
#son.implicit()


#------B) Override explicitly--------
#class Parent(object):
	
#	def override(self):
#		print "parent override()"
		
#class Child(Parent):
	#creating a function in the child class that has the same structure as the parent class
	# but gives a different output
#	def override(self):
#		print	"Child override()"

#dad = Parent()
#son = Child()

#dad.override()
#son.override()

#---------C) Alter before and after
#class Parent(object):
	
#	def altered(self):
#		print "parent altered()"
	
#class Child(Parent):

#	def altered(self):
#		print "Child, before parent altered()" #has a different output from parent class
#		super(Child,self).altered() #supersedes your definition to one for parent class, prints parent
#		print "Child superceded to parent altered()"
	
#dad = Parent()
#son = Child()
	
#dad.altered()
#son.altered()

#---- D) Composition------------
class Other(object):
#create 3 functions in this class
	def override(self):
		print "Other override()"
		
	def implicit(self):
		print "Other implicit()"
		
	def altered(self):
		print "Other altered()"
		
class Child(object):
#Initialize the meaning of self.other, so it can be used in the functions below
#Need to use to get information from Other class, since Child is not a subclass of Other 
	def __init__(self):
		self.other = Other()
		
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print "Child override()"
		
	def altered(self):
		print "Child, before other altered"
		self.other.altered()
		print "Child, after other altered()"
	
son = Child()
son.implicit()
son.override()
son.altered()

#STyle guide https://www.python.org/dev/peps/pep-0008/
# To edit page guide go to preferences and switch to 80 characters