# this is the 2nd exercise i made which will greet u as per your timezone
import time
name = input("Enter your name: ")
a = int(time.strftime('%H'))
if (a >= 12):
    if (a > 12 and a < 15):
        print("Good Afternoon ", name)
    elif(a > 15 and a < 23):
        print("Good Evening ", name)
elif(a > 0 and a < 4):
    print(name ," you should sleep its late")
elif(a > 4 and a < 12):
    print(" Good Morning ", name)
else: 
    print("hello!", name)

# done by shashwat on 19th july 2026
