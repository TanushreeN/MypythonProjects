#to check whether the given year is leap year or not
a = int(input("Enter the Year : "))
if(a % 4 == 0):
    print(str(a) + " " + "is Leap year")
else:
    print(str(a) + " " + "is not a Leap year")
