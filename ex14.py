from sys import argv

script, user_name, food = argv
prompt = 'Your answer please. '

print " Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

print " Is you favorite food %s?" % food
print "Did I guess it correctly?"
guess = raw_input(prompt)
if guess == 'yes': # to have answer be a yes/no in for loop need to set raw_input() == string!
        print 'Yeah'
else:
	print 'Boo' 