# 1) try and except

# try:
#     age = int(input("Enter ur age: "))
#     print(age)
# except ValueError:
#     print("Invalid value plzz insert correct value")

# try :
#     age = int(input("Enter ur age: "))
#     income = 20000
#     risk = income/age
#     print(risk)
# except ValueError:
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Age cannot be 0 ")

phone = int(input("PhoneNo: "))
digits_mapping =""
if phone in digits_mapping:
    digits_mapping = { "1" : "One", "2":"Two", "3":"Three", "4": "Four"}
    output = ""
else:
    output = ("!")
print(output)
# for ch in phone:
#     output += digits_mapping,get(ch,)