tabby_cat = "\tI'm tabbed in." #\t tabs in a line
persian_cat = " I'm split\non a line." #\n makes a new line
backslash_cat = "I'm \\ a \\ cat." #\\ in a string creates a single backslash (see ex10 
# on Learn Python the hard way for a list of escape sequences

fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishes
\t* Catnip\n\t* Grass
""" #\t* tabs in line and * is used as a buller point

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat 

while False: # switching from True to False lets the for loop stay in the code but not run
	for i in ["/" , "-" , "|" , "\\" , "|"]:
		print "%s\r" % i, #comma at end makes this print out on same line. This is a 
		# runaway for loop. To stop it hit control C or type sys.exit 
		
print " This list %s\n\t is for a fat ass cat!" % fat_cat