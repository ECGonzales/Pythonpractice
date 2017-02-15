#*******Dictionaries!*********
# Creating a mapping of state to abbreviations
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI',
	'Virginia': 'VA'
}		 

#Create a basic set of states and some sites in them	
cities = {
	'CA' : "San Francisco",
	"MI": "Detroit",
	"FL": "Jacksonville"
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['VA'] = 'Virgina Beach'

#print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#print every state abreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
#print every city in state
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# Now  do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviaited %s and has city %s" % (state, abbrev, cities[abbrev])
	
print '-' *10
# safely get an abbreviation by state that might not be there
state = states.get("Texas")

if not state:
	print "Sorry, no Texas."
	
#get a city with a default value
city = cities.get('TX', 'Does not exist')
print "The city for the state 'TX' is : %s" % city 

#trying a new one.
state = states.get("Virginia")
print "The city for the %s is %s." % (state, cities[state])

#Another example from http://www.tutorialspoint.com/python/python_dictionary.htm
#dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

#del dict['Name']; # remove entry with key 'Name'
#dict.clear();     # remove all entries in dict
#del dict ;        # delete entire dictionary

#print "dict['Age']: ", dict['Age']
#print "dict['School']: ", dict['School']


#****Making a dictionary with multiple values for the same key
dicts = {'Name': ["Angel", "May", "Betty"], "Age": [12, 11, 10]}
print dicts['Name']
print dicts['Name'][0] #print the first name in the list within the dictionary
print dicts.keys() # tells me what the keys (names to looks up something) are