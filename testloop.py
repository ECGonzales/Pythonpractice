def my_loop(max, current=0, increment=1, numbers=[]):
    for x in range(current, max, increment):
        print "at the top, current is %d" % current
        numbers.append(current)

        increment = int(raw_input("Increase > "))
        current += increment

        print "numbers is now: ", numbers
        print "at the bottom current is %d" % current
        break

    if current < max:
        my_loop(max, current, increment, numbers)
    else:
        print "no more iterating!"


max = int(raw_input("Type in max value for the loop > "))    

my_loop(max)