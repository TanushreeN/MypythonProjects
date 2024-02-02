                 #SWAP CASE 1a
#text = input("Enter the text : ")
# swap_case = text.swapcase()
# print(swap_case)
                        # 1b
# def swap_case(s):
#     return s.swapcase()
#
# if __name__ == '__main__':
#     s = input("ENTER UR NAME : ")
#     result = swap_case(s)
#     print(result)

                                        # 2 FACTORIAL
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# Number = int(input("Enter the number : "))
# result = factorial(Number)
# print(f"The factorial of {Number} is {result}")

                            # 3. Reverse string
def reverse(s):
    return s[::-1]

string = input("Enter a string : ")
result = reverse(string)
print(f"The factorial of {string} is {result}")
