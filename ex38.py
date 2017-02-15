ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)
	
print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # last element in the list
print stuff.pop() #print last element in the list and then remove it
print ' '.join(stuff) #print the list and add a space between each element
print '#'.join(stuff[3:5]) #take the third element and add # between it and the 
						   #fourth element. Print that.

cards = ["A", "K", "Q", "J", 10, 9 ,8, 7, 6, 5, 4, 3, 2, 1]

print cards[6]
thingys = ["hi", "bye"]

if len(cards) != 10: # can't write a for loop instead of a while with this syntax. 
#Needs to be in a range that can be looped over i.e for stuff in range(0,10):
	print len(cards)
	if len(cards) == 14:
		cards.append(thingys[0])
		print cards
	else:
		cards.append(thingys[1])
		
		 
	
