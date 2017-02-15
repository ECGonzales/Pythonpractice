from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	choice = raw_input("> ")
	#if "0" in choice or "1" in choice: #In only need that to appear somewhere in value
	
	#A better way to do this is to check that it is a digit
	if choice.isdigit():
	#Another way to do this is to use a try
	#try:
	#	how_much = int(choice)
	#except ValueError:
	#	dead("Man, learn to type a number.")
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is on front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True: #While true creates infinite loop so you can go through choices again.
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can now go through."
			bear_moved = True #makes bear now move after this choice
		elif choice =="taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.") #ends game because bear
		elif choice == "open door" and bear_moved:					#already moved
			gold_room()
		else:
			print "I got no idea what that means."
			
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever startes at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	choice = raw_input("> ")
	
	if "flee" in choice: #if flee is anywhere in my answer do this
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()
		
#define what my comments for dead mean.
def dead(why):
	print why, "Good Job!"
	exit(0) #closes out code
	
#Define start of game.
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")
		
start()


