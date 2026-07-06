# day 10 match-case statements 
x = int(input("enter a number: "))
match x:
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!= 90:
        print("x is not 90")
    case _ if x!= 80:
        print("x is not 80")
    case _:
        print(x)

# this is all about match-case statements in python 3.10 and above by shashwat on 6 july