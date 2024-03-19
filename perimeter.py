Shape = input("Enter the shape: ").lower()
class Area_Perimeter:
    # to find area and perimeter of circle
    def circle(self):
        radius = int(input("Enter the Radius: "))
        area = 3.14 * radius * radius
        perimeter = 2 * 3.14 * radius
        print("The area of Circle is", area)
        print("The Perimeter of circle is", perimeter)

    def rectangle(self):
        l = int(input("Enter the Length: "))
        b = int(input("Enter the Breadth: "))
        area = l * b
        perimeter = 2 * (l + b)
        print("The area of rectangle is", area)
        print("The Perimeter of rectangle is", perimeter)

    def triangle(self):
        b = int(input("Enter the Base: "))
        h = int(input("Enter the height: "))
        a = int(input("Enter the 1st side length: "))
        c = int(input("Enter the 2nd side length: "))
        perimeter = a + b + c
        area = 0.5 * b * h
        print("The area of triangle is", area)
        print("The Perimeter of triangle is", perimeter)

    def square(self):
        s = int(input("Enter the side: "))
        area = s * s
        perimeter = 4 * s
        print("The area of square is", area)
        print("The Perimeter of square is", perimeter)


# area_prm = Area_Perimeter()
# area_prm.circle()
# area_prm.square()
# area_prm.rectangle()
# area_prm.triangle()

