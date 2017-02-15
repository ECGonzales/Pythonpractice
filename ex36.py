#To try to do while I am away at momma's.
#Create a game like the one from exercise 35. Use lists(ex 32,33,34), functions(sheet), 
#and modules(ex 13)
from sys import exit

#Define how you die in game
def dead(explain):
	print explain, "That sucks!"
	exit(0)

#Define how you win
def win(explain):
	print explain, "You win!"
	exit(0)

#define start of game
def start():	
	print "You and a friend are about to head out on a road trip."
	print """It will be the greatest journey ever. 
	However you and your friend never discussed where you were going. 
	Which direction will you choose to travel in north or south?"""

	choice = raw_input(">>")

	if choice == "north" or choice == "N":
		northpath()
	elif choice == "south" or choice == "S":
		southpath()	
	else:
		print "You only have those choices."
		
#*****************Going north********************************************************
def northpath():
	print "Alright northeast or northwest?"
	
	choice = raw_input(">>")
	
	if choice == "northeast" or choice == "NE":
		dead("You crash into a snow bank and die.")
	elif choice == "northwest" or choice == "NW":
		print "Ok. You were traveling along all hapiliy and then ..."
		print "You hit a pot hole and get a flat tire."			
		print "There is a gas station 2 miles away that does repairs."
		print "Your buddy says he has AAA and would prefer to call them."
		print "Do you call AAA or walk to the gas station?"
			
		choice = raw_input(">>")
			
		if "AAA" in choice:
			print "Your buddy lost his AAA card."
			print "He needs to look up the number on his phone."
			AAAproblem()
				
		elif "gas station" in choice:
			gasstaion()
		else:
			dead("Well it took you too long to agree on what to do. Bear attacks.")	
	else:	
		print "testing2"

		
#AAA		
def AAAproblem():
	print "Do you guys have cell service here?"
	
	choice = raw_input(">>")
	
	if choice == "yes":
		print "There are two numbers that show up:"
		numbers = ["1-800-995-2247", "1-800-937-4245"]
		print numbers
		print "which number do you call?"
		
		choice = raw_input(">>")
			
		if choice == numbers[1]:
			print "That number is no longer in service."
			print "After you get off the phone you see a strange van."
			print "On the side is says 'Rare pokemon inside'."
			print "Your friend walks over while playing Pokemon Go."
			print "You join too."
			dead("Well that kidnapping was simple!")
		elif choice == numbers[0]:
			print "Hello how can we help you?:"
			AAAcall()
		else:
			print "incorrect number"
			AAAproblem()
	elif choice == "no":
		print "Well I guess you have to walk to the gas station"
		gasstation()
	else:
		print "Not an option."


#AAA call
def AAAcall():
	choice = raw_input(">>")
	
	if "flat" or "tire" in choice:
		print "We will send a truck out right away."
		print "When AAA gets there, you ask if they can drop you off after the car is taken to the shop."
		print " Mandy, the AAA agent says 'No problem!'"
		print "You get dropped off at a 5 star cabin resort."
		win("Wow what a trip!")
	else:
		print "I'm sorry could you repeat that"
		AAAcall()		


#Gas Station	
def gasstation():
	print "Following the crooked road down the way you see a sign,"
	print "that says 'Now entering Town of Schuyler.'"
	print "Once you get to the gas station you really have to pee."
	print "The cashier hands you the key and says it is around back."
	print "As you close the bathroom door you see something strange run by."
	print "what do you do?"
	
	choice = raw_input(">>")
	
	if "run" in choice:
		print "They caught you."
		dead("Umm you look so tasty. You're dinner!")
	elif "hide" in choice:
		print "Your friend is worried. You have been gone for a long time."
		print "He walks towards the bathroom"
		dead("A machte cuts though his neck. You're next!")
	else:
		dead("Death by a massive turd!")	

			
#**************************going South**************************************************
def southpath():
	print "Now you are heading down I-95"



start()

