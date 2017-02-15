from sys import argv # argv is what ever arguments you would like to import from your script

script, first, second, third, fourth = argv # tells you what your arguments are. You give 
#your script inputs on the command line when initially running the code

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("how you doin")

print "The fourth variable is a user input: %s" % fourth # when using raw_input() don't 
#forget that the print statement needs to know what type of format it is i.e string, number


#to run script in command line: python ex13.py var1 var2 var3