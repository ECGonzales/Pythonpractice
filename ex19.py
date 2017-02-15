def cheese_n_crackers(cheese_count, boxes_o_crackers):
	print "You have %d chesses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_o_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
print "We can jusr give the function numbers directly:"
cheese_n_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_n_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside too:"
cheese_n_crackers(10 + 20, 5 + 6)

print "We can combine the two and a raw input!:"
fat_kids_extra = int(raw_input("How much fatty?"))
cheese_n_crackers(amount_of_cheese + 100, amount_of_crackers + fat_kids_extra + 1000)


