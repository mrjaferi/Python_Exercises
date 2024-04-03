side1, side2, side3 = input().split(" ")
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

Sum = side1 + side2 + side3

if side1 != 0 and side2 != 0 and side3 != 0:
    if side1 == 90 or side2 == 90 or side3 == 90:
        if Sum % 180 == 0:
            print("Bale")
    else:
        print("Na")
else:
    print("Na")
