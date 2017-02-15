from sys import argv

script, filename = argv

print "We're goint to erase %r." % filename #The filename you give it doesn't need to 
# exist already
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit return."

raw_input('?')

print "Opening the file..."
target = open(filename, 'w') # could add a modifier such as + so I can open file in
# write and read modes

print "Truncating the file. Goodbye!"
#target.truncate() #This isn't needed because opening in w mode will overwrite the entire 
# file => redundant!

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "I'm going to write the file."

target.write("%s \n%s \n%s \n" % (line1, line2, line3)) #to write multiple lines with one
#.write() command keep %s beside \n to make no white space when starting new line
#target.writelines([line1, line2, line3]) another way to write with one command

#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally close the file."
target.close()

targetnew = open(filename) # default is read mode
print targetnew.read() # if you want to have it read the file, it needs to be done after 
# closing it so you can see the changes

