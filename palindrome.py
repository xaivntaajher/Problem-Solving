# Palindrome
# A “palindrome” is a word, phrase, or sequence that reads the same backward as forward i.e. madam	
# Write code that takes a user input and checks to see if it is a Palindrome and reports the result



word = input('Enter a word: ')

words = ''

for index in range(len(word)-1,-1,-1):
    words += word[index]

if words == word:
    print('It is a palindrome')
else:
    print('it is not a palindrome')





