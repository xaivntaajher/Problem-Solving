# Reverse a String



# def reverse_word():

#     word = input('Enter a word: ')

#     reversed_word = ''

#     for index in range(len(word)-1,-1,-1):
#         reversed_word += word[index]

#     print(reversed_word)

# reverse_word()

file_gfg = input('enter word')

result = ""  
file_gfg = open('temp.txt', 'r')
for line in file_gfg:
    g = line.split()
    for elem in g:
        # capitalize first letter of each word and add to a string
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
 
print(result)