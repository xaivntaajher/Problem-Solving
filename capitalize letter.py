# Capitalize a Letter
# Write code that takes a string as input and capitalize the first letter of each word. 
# Words will be separated by only one space. i.e. “hello world” should be outputted as “Hello World”


# takes a string as input. (input function)
# capitalize first letter of each word. .capitalize() function, .upper() function
# words separated by only one space. concatenate


def word(first_word, second_word):

    capitalized_word = ''
    
    capitalized_word = first_word.capitalize() + ' ' + second_word.capitalize()
        
    return capitalized_word
    
word('hello','world')




# word1 = 'hello'
# word2 = 'world'

# capitalized_word = word1.capitalize() + ' ' + word2.capitalize()
    

# print(capitalized_word)

