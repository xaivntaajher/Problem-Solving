# Reverse a String

word = input('Enter a word: ')

def words():
    reversed_word = ''

    for index in range(len(word)-1,-1,-1):
        reversed_word += word[index]

    print(reversed_word)

words()