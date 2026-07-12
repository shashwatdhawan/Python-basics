# day 11 of python learning
# topic: for loop
name = "Python"
for i in name:
    print(i)
    if(i == "y"):
        print("This is the second letter of the word")

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# for k in range(5):
#     print(k) # it will print 0 to 4
# # if we want 1 to 5 then
# for k in range(5):
#     print(k + 1) # it will print 1 to 5
# for k in range(1, 9):
#     print(k) # it will print 1 to 8
for x in range(1, 10, 2):
    print(x) # it will print 1, 3, 5, 7, 9

# this is all about for loop in python. we will learn more about it in the next days.