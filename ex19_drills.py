from sys import argv

script, number1, number2 = argv

def add(a, b):
    print("a+b: %d" % (a+b))

x = 3
y = 4
prompt = '> '

add(1, 1)
add(x, y)
add(1 + 1, 2 + 2)
add(1 + x, 1 + y)
add(int(input(prompt)), int(input(prompt)))

m = input(prompt)
n = input(prompt)
add(int(m), int(n))

add(int(number1), int(number2))
