#assignment2.py - Looping it all up


"""
Take the code you made for Python 2 and put it into a loop that repeats until the user says they want to end the program.
"""

fullName = input("Enter your full name: ")
studentID = input("What is your student ID?: ")
gradYear = input("What year will you graduate?: ")

num1 = input("This semester, how many classes are you taking you take that are 1 credit hour?: ") 
num2 = input("This semester, how many classes are you taking you take that are 2 credit hours?: ")
num3 = input("This semester, how many classes are you taking you take that are 3 credit hours?: ")
num4 = input("This semester, how many classes are you taking you take that are 4 credit hours?: ")

creditHours = int(num1) + (2 * int(num2)) + (3 * int(num3)) + (4 * int(num4))
int(creditHours)

print("Hello " + fullName + ", your student ID is " + studentID + " and you will graduate in " + gradYear + ".")

if creditHours > 12:
    print("You are taking " + str(creditHours) + " credit hours this semester, you're doing great! Keep it up!")
elif creditHours < 9:
    print("You are taking " + str(creditHours) + " credit hours this semester, you could do better than that! :(")
else:
    print("You are taking " + str(creditHours) + " credit hours this semester, you're doing okay.")