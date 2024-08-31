"""
x = 0 #false
y = 3 #true
print(x or y)

x = 2
y = 4
print(x or y)

x = 2
y = 4
y += 1

print(y)

x = 5
y = x % 2 #2r1
print(y)


x = 7
y = x // 2 #/ float #// int
print(y)

#Create a program that accept integer from user, then prints whether the integer is an Odd number or Even number.
number = int(input("Pick a number: "))

if number % 2 == 0:
    print("Its an even number")
else:
    print("its an odd number")    

#Create a Program that checks if user is eligible to vote or not. Take note, that 12 years upward is the eligible age to vote. 
age = int(input("how old are you:  "))  
if age > 11:
    print("You are eligible to go and vote") 

else:
    print("Your are not eligible to go and vote ")


rain = ["jan", "feb", "mar", "apr"]
print(rain[-4])
"""

x = "8"
y = "0"
z = int(x + y)
print(z * 2)

x = 20
y = 15
z = int(x < y)
print(not(z))

#Expected out is 'True'