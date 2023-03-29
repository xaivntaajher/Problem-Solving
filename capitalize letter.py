# Capitalize a Letter
# Write code that takes a string as input and capitalize the first letter of each word. 
# Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”
# capitalize, .upper()

# takes a string as input. (input function)
# capitalize first letter of each word. .upper() function
# words separated by only one space. concatanate


def word(word1, word2):

    word1 = ''
    word2 = ''
    for num in range(len(word1),len(word2)):
        capitalized_word = word1.upper(num[0]) + ' ' + word2.upper(num[0])
        
    return capitalized_word
    
word('hello','world')




# def reverse_word(word):

#     reversed_word = ''
    
#     for index in range(len(word)-1,-1,-1):
#         reversed_word += word[index]

#     return reversed_word

# reverse_word('pineapple')