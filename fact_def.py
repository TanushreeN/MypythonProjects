def factorial(num):
    result = 1
    for i in range (1,num+1):
        result *= i
    return result
    
num = int(input("Enter a number: "))
print(f"The Factorial of {num} is:", factorial(num))

# __________________________
#OP:    Enter a number: 5
#       The Factorial of 5 is: 120
