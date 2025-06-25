def calc():
    x = int(input("1 add 2 sub 3 mul 4 div: "))
    if x == 1:
        a = float(input("a: "))
        b = float(input("b: "))
        print("a+b=", str(a+b))
    if x ==2:
        a = float(input("a: "))
        b = float(input("b: "))
        print("a-b=", str(a-b))
    if x ==3:
        a = float(input("a: "))
        b = float(input("b: "))
        print("a*b=", str(a*b))
    if x ==4:
        a = float(input("a: "))
        b = float(input("b: "))
        print("a/b=", str(a/b))
        if b != 0:
            print("a/b=", str(a/b))
        else:
            print("cannot divide by zero")
calc()

