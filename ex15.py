#One method of getting a file is using argv
from sys import argv

script, filename = argv
txt = open(filename) #defines the file that I want opened to be called txt

print "Here is your file %r:" % filename
print txt.read() # prints out the txt file in the command line
txt.close() #closes file

#Another method of reading a file using raw_input.
print "Type the filename again:"
file_again = raw_input(">") # asks the user which file to look at

txt_again = open(file_again, "r+") #opens file to go to a different directory than one 
# working in use ../ or /Users/EileenGonzales/whereyouarelooking
# "r+" opens file for reading an writing no quotes around file_again since it is a variable
# more about file types: https://docs.python.org/2/tutorial/inputoutput.html

txt_again.write(raw_input()) #lets me manually input the additional text to the file
print txt_again.read() #prints file
txt_again.close()

# to read file while in python shell use
# f = open('workfile', 'w')
# f.read()