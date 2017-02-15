# This one is like my scripts with argv
def print_two(*args): #defining the function named print_two
	arg1, arg2 = args #need to indent all the following lines so they are attached to this def.
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#Ok, that *args is pointless, we can just do this
# Creating a function that prints two things
def print_two_again(arg1, arg2): # easier to do than lines 2 and 3
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#This one takes only 1 argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#This one takes none
def print_none():
	print " I get nada."
	
print_two("boo","gers")
print_two_again("boo","gers")
whatisaid = raw_input("what would you like to see me print?")
print_one(whatisaid*5)
print_none()
