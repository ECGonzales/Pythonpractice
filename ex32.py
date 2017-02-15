the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes',3, 'quarters']

#This first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number

#sam as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#Also we can go through mixed lists too
#Notice we have to use %r since we don;t know what's in it
for i in change:
	print "I got %r" % i
	
#We can also build lists, first start with an empty one
elements = []

#Then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
#Now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
#Another way to create a list without using a for-loop if it is just numerical values
newlist = range(0,10,2)
print newlist

#More ways to genterate a list
elements1 = [0,1,2,3,4,5,6,7,8,9,10]

elements1[3:5] = range(10,12) # replace indexes 3 and 4 with 10 and 11.
print elements1[3:5]
elements1[3:7:2] = range(100,201,100) #replace indexes 3 and 5 with 100 and 200
print elements1[3:7:2]
elements1[:] = range(4) # replace entire list with [0,1,2,3]