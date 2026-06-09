# day 4 of python learning
# Typecasting in python programming
# by shashwat on 9th june 2026

# typecasting is the process of converting one data type to another data type
# for example:
a = "10"
b = "11"
print(int(a) + int(b)) 
# in the above code we have converted the string data type to integer data type using int() function and then added them

# typecasting are of 2 types:
# 1. implicit typecasting
# in implicit typecasting the python automatically converts one data type to another data type but there's a catch the data type will be converted to the higher data type
# for example:
c = 10
d = 10.5
print(c + d)
# in the above code we have added an integer and a float and the result is a float because the float data type is higher than the integer data type

# 2. explicit typecasting
# in explicit typecasting we manually convert one data type into another data type using functions like int(), float(), str() etc.
# for example:
e = True
f = "i am older than 18"
print(f + ", " + "is", str(e))
# in the above code we have converted the boolean data type to string data type using str() function and then concatenated it with another string
print(" so thats how we use typecasting in python programming" , "\n", end=" by shashwat on 9th june 2026")