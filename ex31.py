print " You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(">")

if door == "1":
	print "There's a giant bear hiding here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input(">")
	
	if bear == "1":
		print " The bear eats your face off. Good Job!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
		print " Now that you've scared off the bear you see a path through the trees."
		print " Do you: 1. go after that bear or 2. Go down the path."
		
		decision = raw_input(">")
		
		if decision == "1":
			print "The bear comes running at you with avengence."
			print "He tells you to give him $30 or die."
			print "How much do you have?"
			
			money = int(raw_input(">"))
			
			if money in range(1,29):
				print "Bear kills you."
			elif money >= 30:
				print "Bear is happy that you obeyed."
			#else:
			#	print "Exactly what I asked for."
				
		elif decision == "2":
			print " Stop to check code."
elif door == "2":
	print "You stare into the endless abysss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input(">")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
	else:
		print "The insanity rots your eyes into a pool of muck. God Job."
		
else:
	print " You stumble around and fall on a knife and die. Good Job!"
