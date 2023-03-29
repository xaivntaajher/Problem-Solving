# Reverse a String



def reverse_word(word):

    reversed_word = ''
    
    for index in range(len(word)-1,-1,-1):
        reversed_word += word[index]

    return reversed_word

reverse_word('pineapple')


