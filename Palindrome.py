val = input("Enter a string : ")
str_val = str(val)
if str_val == str_val[::-1]:
    print(val, "is a palindrome")
else:
    print("Not a Palindrome")