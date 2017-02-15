from sys import argv

script, input_file = argv

#defining a function that prints out your entire file
def print_all(f):
	print f.read()

#defining a function that goes to the 0th byte in the file (start of file)	
def rewind(f):
	f.seek(0)

# A function that prints out a line of your code and which line number it is
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1 # += adds one to previous definition of current_line
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)


#Using a for loop to print all 3 lines in the code with their line number
print " Now let's try a for loop!"
rewind(current_file)
for current_line in range(1,4): #need to go one line beyond total line numbers to get all
								# lines printed. If go range(1,3) only get lines 1 and 2.  
	print_a_line(current_line, current_file)


