tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

formatter = "%r %r %r %r"

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#%r is printing out the raw data
print(formatter % (tabby_cat, persian_cat, backslash_cat, fat_cat))


while True:
    for i in ["/","-","|","\\","|"]:
        print("%s\r" % i, end=' ')
