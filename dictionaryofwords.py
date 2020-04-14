"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Abracadabra"] = "a word said by magicians when performing a magic trick."
word_definitions["Coffee"] = "a hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

print(word_definitions["Awesome"])
print(word_definitions["Coffee"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word,definition) in word_definitions.items():
    print(f'The definition of {word} is: {definition}')