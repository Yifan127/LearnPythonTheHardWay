my_name = 'Yifan Zhang'
my_age = 33 #not a lie
my_height = 161 #centimeters
my_weight = 52 #kilograms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = "Black"

my_height_inches = my_height * 0.39
my_weight_pounds = my_weight * 2.2

print("Let's talk about %s." %my_name)
print("She's %.2f cm (%.2f inches) tall." %(my_height, my_height_inches))
print("She's %.2f kg (%.2f pounds) heavy." %(my_weight, my_weight_pounds))
print("Actually that's not too heavy.")
print("She's got %s eyes and %s hair." %(my_eyes,my_hair))
print("Her teech are usually %s depending on the coffee." %my_teeth)

#this line is tricky, try to get it exactly right
print("If I add %.2f, %.2f, and %.2f I get %.2f." % (
my_age, my_height, my_weight, my_age + my_height + my_weight))
