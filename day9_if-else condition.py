# day 9 of python learning 
# topic:- if-elif-else-nested conditions

# if condition
a = int(input("Enter your number: "))
if (a < 0):
    print(" Number is negative!")
else:
    print(" Number is positive!")
print("Yayyy")

# if-elif condition
b = int(input(" Enter your age: "))
if (b >= 18):
    print("You can vote now")
elif(b <= 0):
    print(" Its invalid run terminal again ")
else:
    print(" Too Young")

# if-elif-nested condition 
c = int(input("Enter your age again: "))
if (c >=18):
    print("You are now eligible to drive")
elif(c <= 18):
    if (c > 16 and c < 18):
        print(" You have to wait to drive till you turn 18")
    elif(c < 16):
        print("You are too young to drive ")
else:
    print("Sorry U are AI :)")

# conditional operators 
# >,<,>=,<=,==,!=
# the conditional operators return the answer in boolian type
print(" this is all i have done in day 9 by shashwat on 19th july 2026")