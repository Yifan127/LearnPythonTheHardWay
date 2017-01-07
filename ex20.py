from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

# set the file's current position
# Each time you do f.seek(0) you're moving to the start of the file.
def rewind(f):
    f.seek(0)

#Each time you do f.readline() you're reading a line from the file,
#and moving the read head to right after the \n
#The readline() function returns the \n that's in the file at the end of that line.
#Add a , at the end of your print function calls to avoid adding double \n to every line.
def print_a_line(line_count, f):
    print(line_count, f.readline(), end=' ')

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print thress lines:")

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line+=1
print_a_line(current_line, current_file)

current_line+=1
print_a_line(current_line, current_file)

current_file.close()
