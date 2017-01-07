number = []
i = 0

def while_ex (stop, step):
    global i
    while i < stop:
        print("At the top i is %d" % i)
        number.append(i)

        i += step
        print("Number now: ", number)
        print("At the bottom i is %d" % i)

    print("The numbers:")

    for num in number:
        print(num)

def for_ex(stop, step):
    for i in range(stop, step):
        print("At the top i is %d" % i)
        number.append(i)

        print("Number now: ", number)
        print("At the bottom i is %d" % i)

    print("The numbers:")

    for num in number:
        print(num)

while_ex(10, 3)
for_ex(10, 3)
