import random
#
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "Class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameter.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameter self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    # strip() is to remove space char from the beginning and the end of string
    # bytes.decode(): from bytes to string
    # str.encode(): from string to bytes
    WORDS.append(word.strip().decode())

def convert(snippet, phrase):
    # capitalize the first character
    # random.sample(s,k): return a k length list of unique elements chosen from s
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    # print("class_names: {0}".format(class_names))
    other_names = random.sample(WORDS, snippet.count("***"))
    # print("other_names: {0}".format(other_names))
    results = []
    param_names = []

    # range: select a number in 0<= number < snippet.count("@@@")
    for i in range(0, snippet.count("@@@")):
        # return a integer : 1<=integer<=3
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
        # print("param_names: {0}".format(param_names))

    for sentence in snippet, phrase:
        # copy sentence to result, it's more readable to write like this result = list(sentence)
        result = sentence[:]
        # print("copy the sentence to result: {0}".format(result))

        # fake class names
        for word in class_names:
            # replace '%%%' with word, restricting the number of replacemnet to once
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-C
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(list(snippets))

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER: {0}\n\n".format(answer))
except EOFError:
    print("\nBye")
