def date():
    thirtyone = [1, 3, 5, 7, 8, 10, 12]
    thirty = [4, 6, 9, 11]
    global y
    y = int(input("month? "))
    global z
    z = int(input("day? "))
    print(" ")
    if y in thirtyone and z in range(1, 32):
        sign()
    elif y in thirtyone and z not in range(1, 32):
        print("not a real date. try again please!")
        print(" ")
        date()
    elif y == 2 and z in range(1, 30):
        sign()
    elif y == 2 and z not in range(1, 30):
        print("not a real date. try again please!")
        print(" ")
        date()
    elif y in thirty and z in range(1, 31):
        sign()
    else:
        print("not a real date. try again please!")
        print(" ")
        date()
def sign():
    if y == 1:
        if z < 21:
            print("capricorn")
        else:
            print("aquarius")
    if y == 2:
        if z < 19:
            print("aquarius")
        else:
            print("pisces")
    if y == 3:
        if z < 21:
            print("pisces")
        else:
            print("aries")
    if y == 4:
        if z < 21:
            print("aries")
        else:
            print("taurus")
    if y == 5:
        if z < 22:
            print("taurus")
        else:
            print("gemini")
    if y == 6:
        if z < 22:
            print("gemini")
        else:
            print("cancer")
    if y == 7:
        if z < 23:
            print("cancer")
        else:
            print("leo")
    if y == 8:
        if z < 23:
            print("leo")
        else:
            print("virgo")
    if y == 9:
        if z < 23:
            print("virgo")
        else:
            print("libra")
    if y == 10:
        if z < 23:
            print("libra")
        else:
            print("scorpio")
    if y == 11:
        if z < 22:
            print("scorpio")
        else:
            print("sagittarius")
    if y == 12:
        if z < 21:
            print("sagittarius")
        else:
            print("capricorn")
    print(" ")
    date()  
date()
