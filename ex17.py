from sys import argv
from os.path import exists #exists prints True if file exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

#do in one line?
#in_file = open(from_file).read()
#in_file = open(from_file) (1)
#indata = in_file.read() (2)

#extraneous output!
#print " The input file is %d bytes long" % len(indata)
#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continuem CRTL-C to abort."
#raw_input()

#out_file = open(to_file, 'w')
#out_file.write(in_file)


#out_file.close()
#in_file.close() do not need when combining (1) and (2) file eventaully closes!


# A better way to do all of this in one line is
with open(from_file) as in_file, open(to_file, 'w') as out_file:
	out_file.write(in_file.read())
# Gaurenteed to close files!

# Eileens-MacBook-Pro:Pythonpractice EileenGonzales$ echo "This is a test file." >test.txt
# Eileens-MacBook-Pro:Pythonpractice EileenGonzales$ cat test.txt
# This is a test file.

# See appendix A for more on how to do this
# More on import see https://www.codementor.io/python/tutorial/python-path-virtualenv-import-for-beginners