# A prime number is a number that is only divisible by one and itself.
# Write a method that prints out all prime numbers between 1 and 100 
# for loop range
# conditionals


for number in range(1,101):
    if number > 1:
        for num in range(2, number):
            if (number % num) == 0:
                break
            else:
                print(number)
