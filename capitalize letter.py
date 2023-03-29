# Capitalize a Letter
# Write code that takes a string as input and capitalize the first letter of each word. 
# Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
# capitalize, .upper()

word = input('Enter a word: ')

capitalized_word = ''

for index in range(len(word)):
    capitalized_word = word.upper([1])

    print(capitalized_word)

# def words():
#     capitalize_word = ''

#     capitalize_word = word.title()

#     print(capitalize_word)

# words()

print(word.upper())

# def reverse_word():

#     word = input('Enter a word: ')

#     reversed_word = ''

#     for index in range(len(word)-1,-1,-1):
#         reversed_word += word[index]

#     print(reversed_word)

# reverse_word()