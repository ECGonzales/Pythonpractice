#Multiple ways to create and use a while loop
#i = 0
#numbers = []

#while i < 6:
#	print "at the top i is %d" % i
#	numbers.append(i)
#	
#	i = i + 1
#	print "Numbers now:", numbers
#	print "At the bottom i is %d" % i

#print "The numbers: "

#for num in numbers:
#	print num
	
#trying to complete the same task using while loop in function
def buildlist(num):
	numlist = []
	i = 0
	while i < num: #while the value in the while loop is less than the value you give it continue
		numlist.append(i)
		i += 1
		print "i: %d" % i, # comma prints these two on the same line!!!
		print "list:", numlist	
		
#create the list
buildlist(6)


#Another way, which allows you to change the iteration value
def list2(num,x):
	num = int(num)
	numlist1 = []
	i = 0
	while i < num:
		numlist1.append(i)
		i += x #iterate by adding by any value each time to build list.
		print "i: %d" % i
		print "list:", numlist1
		
# running def as a user input
answer = raw_input("Enter a number less than 10:")
x = raw_input("iterate by what increment?")
list2(answer, int(x)) #need to convert input string to numeric value.



#Using for-loops and range
def newlist(num,increment):
	list2 = []
	num = int(num)
	inc = int(increment)
	for i in range(0,num,inc): #To change what you need to increment by this must be
		print "i: %d" % i,     #defined in the range part of the for-loop
		list2.append(i)
		print "numbers now are:", list2
		
#run it
number = raw_input("List up to what value?:")
increments = raw_input("increment by?:")
newlist(number, increments)
