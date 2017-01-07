stuff = {'name':'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])

print(stuff['age'])

print(stuff['height'])

stuff['city'] = "Auckland"

print(stuff['city'])

print(stuff)

stuff[1] = "Wow"
stuff[2] = "Neato"

print(stuff[1],stuff[2])
print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("{0} has the city {1}".format(abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("{0} state is abbreviated {1} and has city {2}".format(state, abbrev, cities[abbrev]))

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {0}".format(city))
