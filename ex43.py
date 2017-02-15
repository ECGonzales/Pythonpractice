from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and use enter()."
		exit(1) #There was some error => closes out code.

# This method starts playing the scenes		
class Engine(object):
	
	def __init__(self,scene_map):
		self.scene_map = scene_map
		
	def play(self):
		#current scene is the opening scene from the map and 
		#the last scene is the final scene in the next scene sequence
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			#next scene is known in the current scene 
			next_scene_name = current_scene.enter()
			#replace current scene with next one from the map.
			current_scene = self.scene_map.next_scene(next_scene_name)
		
class Death(Scene):
	remarks = [ 
		"You died. You kinda suck at this.",
		"Your mom would be proud...if she were smarter.",
		"Such a loser."
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.remarks[randint(0,len(self.remarks)-1)]
		exit(1)
		
class CentralCorridor(Scene):
	def enter(self):
		print "The Gothon of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member anf your last"
		print "mission is to get the neutron destrucy bomb from the Weapons Armory,"
		print "put it in the bridge, anf blow up the ship after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when "
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the "
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input(">")
		
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing anf moving aroind your body, which throws"
			print "off your aim. Your laser hits his costume but missed him entirely. This"
			print "completely ruind his brnad new oufit his mommy bought him, which"
			print "make him fly into an insane rage anf blast you repeatedly in the face untill"
			print "you are dead. Then he eats you. UMMM tasty!"
			return 'death'
			
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past you head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "Your head and eats you. 'Um the taste of human flesh is delious' he exclaims."
			return 'death'
			
		elif action =="tell a joke":
			print "Lucky for you they made you learn Gothon insluts in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lernkjerbg bebfrrhn vb jrebb fjefru nejsvosuhg, ghirhguoa ghja fhjreh."
			print "The Gothon stops, tries not to laugh, then brusts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then jump through the Weapon Armory door."
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!!!"
			return 'central_corridor'
		
class LaserWeaponArmory(Scene):
	def enter(self):
		print "You do a dive roll into the Armory, crouch and scan the room."
		print "It's dead quiet, too quiet. You stand up and run to the far side of the "
		print "room and find the neutron bomb in its container. There's a keypad lock"
		print "on the box and you need to determine the code to get the bomb out."
		print "If you get the code wrong 10 times, it triggers a permant override lock."
		print " The code is three digits."
		#code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		code = "146" #added so that I could actually move on!
		guess = raw_input("[keypad]>")
		guesses = 0
		
		while guess != code and guesses <9:
			print "BZZZECD!"
			guesses += 1
			guess = raw_input("[keypad]>")
			
		if guess == code:
			print " The container clicks open and gas seeps out into the air."
			print " You grab the bomb and book it to the bridge to stick it in the right spot."
			return 'the_bridge'
		
		else:
			print "The lock buzzes one last time as you hear the melting sound of plastic"
			print "fusing together. You decide to sit there and finally the Gothons blow"
			print "up the ship from their command station and you die in a blazing glory of"
			print "saddness and despair."
			return 'death'
				
class TheBridge(Scene):
    def enter(self):
        print "You burst into the Bridge with the neutron bomb under your arm and surpise"
        print "5 Gothons who are trying to take control of the ship. Each of them is even"
        print "uglier than the last. They haven't pulled out their weapons yet, as they"
        print "have spotted the active bomb under your arm."
        
        action = raw_input(">")
        
        if action == "throw the bomb":
        	print "In a panic you throw the bomb at the feet of the Gothons and make a leap"
        	print "for the door. Right as you drop it a Gothon shoots you smack in the "
        	print "middle of the back instanly killing you."
        	print "As you fall to the ground you see the hand of a Gothon trying to disarm"
        	print "the bomb. You die knowing that they will probably blow up when it goes off."
        	return 'death'
        	
        elif action == "slowly place the bomb":
        	print "You point your blaster at the bomb under your arm and the Gothons put"
        	print "their hands up and start to sweat. You inch backward to the door, open"
        	print "it, and then carefully place the bomb on the floor, pointing your blaster"
        	print "at it. You then jumo back through the door, punch the close button and "
        	print "blast the lock so he Gothons can't get out."
        	print "Now that the bomb is in place you run to the escape pod to get off"
        	print "this tin can!"
        	return 'escape_pod'
        	
        else:
        	print "DOES NOT COMPUTE!!"
        	return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print "You rush thorugh the ship desperately trying to make it to the escape pod"
        print "before the ship explodes. It seems like hardly any Gothons are on the ship,"
        print "so your run is clear of interference. You get to the chamber with the"
        print "escape pods, and now need to pick one to take. Some of them could have been"
        print " damaged from this brutle battle, but you don't have time to look. There's"
        print "5 pods, which one do you take?"
        
        good_pod = randint(1,5)
        guess = raw_input("[pod #]>")
        
        if int(guess) != good_pod:
        	print "You jump into pod %s and hit the eject button." % guess
        	print "The pod shoots out of the ship out into the void of space, then suddenly"
        	print "implodes as the hull ruptures, crushing your tiny body into jelly."
        	return 'death'
        else:
        	print "You jump into pod %s and hit the eject button." % guess
        	print "The pod easily slides out into space heading towards the planet below."
        	print "As it flies to the planet, you look back and see your ship implode, "
        	print "then explode like a bright star, taking out the Gothon ship at the same"
        	print "time. You defeated the Gothons!!"
        	return 'finished'
        
class Finished(Scene):        
        def enter(self):
        	print "You won! Good Job."
        	return 'finished'
        
        
class Map(object):
	
	#dictionary of scenes, refer to this by using Map.scenes
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self,start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
			
#Start the game
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()