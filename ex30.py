people = 30
trucks = 15
cars = 20

if cars > people:
	print " We should take the cars" #can use more complex boolean statements to evaluate 
elif cars < people or cars < trucks: #Again elif is "else if" and for a specific situation
	print "We should't take the cars."
else:								# Else covers all other situations
	print "We can't decide."
	
if trucks > cars and cars > people:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."
	
if people > trucks and trucks > cars:
	print "Alright, let's just take the trucks."
else:
	print " Fine, let's stay home then."
