# string methods on 18 july 2026
# string are immutable in python 
a = "hello world"
print(a.upper()) # converts the string into uppercase 
print(a.lower()) # converts the string into lowercase
print(len(a)) # gives the length of the string
str1 = "!!!! hello world !!!!!!!!!!!!!!!!!"
print(str1.rstrip("!")) # removes the trailing characters from the string like ! 
print(a.replace("hello world", "hi everyone")) # replaces all the occurance of a string with another string
print(a.split(" ")) # the split method splits the given string at the specific instance and returns the separated string as list items
heading = "evonix network"
print(heading.capitalize()) # the capitalize method helps turning the first charachter of string to uppercase and rest of characters into lower case . 
print(heading.center(50)) # the centre method alligns the string to the centre as per the given parameters by the user  
print(len(heading))
print(len(heading.center(50))) 
print(a.count("l")) # the count() method return the number of times the given value has occured within the string 
str2 = " hey i am Vrny_ i am learning python !!!"
print(str2.endswith("!!!")) # the endswith() method if the string ends with the given value. if yes then it returns True if not then it returns False
print(str2.endswith("hey"))
str1 = " hey i am john, i am learning a computer language name python ."
print(str1.find("am")) # find() method searches for first occurence of the given value in the string and returns the index where it is present if its not in the string it returns -1.
print(str1.find("strhh")) # here the find() method searches for sthh in the string but there is no value so it returns with -1 .
print(str1.index("hey")) # now the index() method also searches for the first occurance of the given value in the strings and returns with the index where it is present if its not find then it will raise an exeption(error).
# print(str1.index("he0y")) # now it will search for he0y but its not in string so it will raise an exeption .
str3 = "WelcomeTOEvonixNetwo1rk"
print(str3.isalnum()) # it says true now but if we put any space btw the string it will return false [only it will sa true if string has A,Z a,z 0,9] if there is something else it says false
print(str3.isalpha()) # isalpha() method returns true if only the string consists of A,Z or a,z if any other charachter or punctuations are present it returns false.
str1 = "hey, i am john"
print(str1.islower()) # we can overwrite strings too and yea islower() method returns true if all the charachters in string are lower case else it returns false.

str1 = " hey merry christmas, have a happy new year"
print(str1.isprintable()) # now isprintable() method returns true only if the given charachter in string are printable else false 
str1 = " hey \n happy new year"
print(str1.isprintable()) # now it will say false as \n is not a printable 
print(str1)
str1 = "   " # using tab or space  
print(str1.isspace()) # isspace() method will only return true if it has only white space using space bar else it will return false
str1 = " hey    " # not only space but another charachter
print(str1.isspace()) # now isspace() method will return false as it has another charachter instead of space 

str4 = " Hey This Is Evonix Network"
print(str4.istitle()) # istitle() method is used to check if every first letter of the word in a string is capitalized if yes it will return true if not it will return false.
str5 = " hey This Is Evonix network"
print(str5.istitle()) # now istitle() will return false as every first letter in word of string is not capitalized 
str1 = "HEY THIS IS EVONIX NETWORK , DO U NEED ANY HELP SIR"
print(str1.isupper()) # the isupper() method is used to check if every letter in a word is capitalized if yes it will return True if not every word is capitalized then it will return false.
str2 = "hey this is EVONIX NETWORK"
print(str2.isupper()) # now it will print false as every letter is not capitalized in this string
str1 = "hey this is evonix network"
print(str1.startswith("hey")) # startswith() method is used to check if the given string started with the given value if yes then it will return true if not it will return false.
str2 = "hey this is evonix network"
print(str2.startswith("yoo")) # now it will return false as the given string is not started with the given value .
str1 = "hey I aM hArRy anD I am LeaRninG PYthoN"
print(str1.swapcase()) # swapcase() is the method from which we can exchange the cases in string in python if the letter is in uppercase it will be converted into lowercase if something is in lowercase it will be converted into uppercase.
str1 = "Welcome to evonix Network, Hope u have a good day"
print(str1.title()) # title() method is used to capitalize every first letter of word in a string 