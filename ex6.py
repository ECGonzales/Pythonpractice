x = " There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x,y

print " I said: '%r.'" % x
print " I also said: '%s'" % y

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r" # %r is for debugging an shows raw input

print joke_evaluation % hilarious

w = "This is the left side o f..."
e = "a string with a right side."

print w + e