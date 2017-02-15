print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print " So you're %r old, %r tall, %r heavy." % (age, height, weight)

name = raw_input('Enter your Name')
print ( "Hi %s, Let's be friends!" % name);

# Another example that is more complex from: http://www.cyberciti.biz/faq/python-raw_input-examples/
#creates a menu screen
print 30 * '-'
print "  M A I N - M E N U "
print 30 * '-'
print "1. Backup"
print "2. User mangement"
print "3. Reboot the server"
print 30 * '-'

#Creates raw input options
choice = raw_input('Enter your choice [1-3] : ')

choice = int(choice) # coverts string to an integer! could do int(raw_input())

#If statements to determine what to do for each input
if choice == 1:
        print ("Starting backup...")
elif choice == 2:
 		print 'Starting user mangement...'
elif choice == 3:
 		print "Rebooting the server..."
else:
		print 'Invalid number. Try again.'