
while True:
    s = input("Please input a number: ")
    # string.isdigit - Return true if all characters in the string
    # are digits and there is at least one character, false otherwise.
    if s.isdigit():
        s = int(s)
        break
    else:
        print("%s is not a number." % s)

while True:
    try:
        s = input("Please input a number: ")
        s = int(s)
        break
    except ValueError:
        print("%s is not a number." % s)
