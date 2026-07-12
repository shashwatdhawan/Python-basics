# day 13 of python learning 
# topic: break and continue statements in python
for i in range(12):
    if i == 10:
        print("leave the loop and go")
        break
    print(" 5 X", i, "=" , 5*i)
    

for i in range(12):
    if i == 10:
        print("skip the iteration and go to next iteration") 
        continue
    print(" 5 X", i, "=" , 5*i)

# do while loop in python
# to emulate do while loop in python we need to create a while loop with a condition that is always true and then use a break statement to exit the loop when a certain condition is met.
# ex:
while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break
print("You entered a positive number:", number)

# this is all i did in break and continue statements in python