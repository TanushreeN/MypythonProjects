# n = int(input("Enter the Guessed number : "))
# sn = 45
# chance = 6
# if n in range(0, 101):
#     while (chance > 0 and chance < 7):
#         if(n == sn):
#             print("Hurray... Won...!!")
#             print("The secret number is", n)
#             break
#         elif(n < sn ):
#             print("The secret number is greater than",n)
#             break
#         elif(n > sn ):
#             print("The secret number is less than", n)
#             break
#         else:
#             print("You lost...!!!")
#             break

print("Welcome to Tanu's Bowl restorent, here is your Menu\n")
print('''Food       price

1)Poori      30rs
2)Dese       50rs
3)Benne Dose 70rs
4)Open Dose  80rs
5)Iddli      20rs
6)Vada       15rs
         ''')

print("enter 0 for food number if you are done with the order")
total = 0
while True:
    food_num = int(input("enter food number: "))
    if food_num == 0:
        print(f"grand total {total} ")
        break
    quantity = int(input("enter quantity: "))
    if food_num == 1:
        print(f"poori-{quantity}")
        price = 30
        total += price * quantity

    if food_num == 2:
        print(f"Dose-{quantity}")
        price = 50
        total += price * quantity

    if food_num == 3:
        print(f"Benne Dose-{quantity}")
        price = 70
        total += price * quantity

    if food_num == 4:
        print(f"Open Dose-{quantity}")
        price = 80
        total += price * quantity

    if food_num == 5:
        print(f"Iddli-{quantity}")
        price = 20
        total += price * quantity

    if food_num == 6:
        print(f"Vada-{quantity}")
        price = 15
        total += price * quantity