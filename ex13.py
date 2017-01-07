from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


name = input("What's your name? ")
age = input("How old are you? ")

print("Your name is: ", name)
print("You are %r years old." % age)
