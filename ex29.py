print "How many people are there?"
people =int(raw_input("people --->")) #**raw_input gives you a string!! Remember to covert
									  # to an integer if you need it!
cats = 30
dogs = 13

if people is cats:
	print "Too many cats! The world is doomed!"
else: 					# When using if statement if you want a general otherwise and not 
	print "we not cats" # A specific value use else: instead of else if.
	
if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
	
dogs += 5
print dogs

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print " People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."

