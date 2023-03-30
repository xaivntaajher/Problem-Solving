# A prime number is a number that is only divisible by one and itself.
# Write a method that prints out all prime numbers between 1 and 100 
# for loop range
# conditionals
# print


for num in range(1,101):
    is_prime = True
    for num2 in range(2,num):
        remainder = num % num2
        if remainder == 0:
            is_prime = False
            break
    if is_prime:
        print(num)




# modulus
# x = 43
# y = 1
# result = x % y

# print(result)


