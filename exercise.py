### :heavy_plus_sign: Task 1 - calculate sum
### Your task is to write a Python program to calculate the sum of three integers given (prompted) by user.  
### If the values are equal then calculate triple value of their sum.  
### Print out an appropriate message to the user.

#### 1
first_number = 3
second_number = 4
third_number = 5

numbers = [3, 4, 5]
sum(numbers)

first_number = int(input("Enter first umber: ", ))
second_number = int(input("Enter second number: ", ))
third_number = int(input("Enter third number: ", ))
print("The sum is: ", sum(numbers))
if first_number == second_number == third_number:
    print(3 * sum(numbers))
elif first_number != second_number != third_number:
    print("The values of numbers are not equal.")

#### 2
first_number = 5
second_number = 5
third_number = 5

numbers = [5, 5, 5]
sum(numbers)

first_number = int(input("Enter first umber: ", ))
second_number = int(input("Enter second number: ", ))
third_number = int(input("Enter third number: ", ))
print("The triple sum is: ", 3 * (sum(numbers)))

### :heavy_plus_sign: Task 2 - get the difference
### Your task is to write a Python program to get the difference between a two given numbers (prompted by user).  
### If the first number is greater than second then calculate double difference between numbers.  
### Otherwise calculate the **absolute** difference between numbers.  
### Print out an appropriate message to the user.

#### 1
first_number = -2
second_number = -3
numbers = [-2, -3]
first_number = int(input("Enter first umber: ", ))
second_number = int(input("Enter second number: ", ))
print("The results of the calculation is: ", -2 - (-3))
if first_number > second_number:
    print("The double difference of values is:", 2 * (-2 - (-3)))
else:
    print("The absolute difference between he numbers is: ", -2 - (-3))

#### 2
first_number = 6
second_number = 6
numbers = [6, 6]
first_number = int(input("Enter first umber: ", ))
second_number = int(input("Enter second number: ", ))
print("The results of the calculation is: ", 6 - 6)
if first_number > second_number:
    print("The double difference of values is:", 2 * (6 - 6))
elif first_number == second_number:
    print("The absolute difference between the numbers is: ", 0)
else:
    print("Fist number is not greater than second number, but both are equal.")

#### 3
first_number = 4
second_number = 7
numbers = [4, 7]
first_number = int(input("Enter first umber: ", ))
second_number = int(input("Enter second number: ", ))
print("The results of the calculation is: ", 4 - 7)
if first_number > second_number:
    print("The double difference of values is:", 2 * (4 - 7))
elif first_number < second_number:
    print("The absolute difference between the numbers is: ", 4 - 7)
else:
    print("Fist number is not greater than second number, but smaller.")
    
### :heavy_plus_sign: Task 3 - odd or even number
### Your task is to write a Python program to find whether a given number (prompted from the user) is even or odd.  
### Print out an appropriate message to the user.

#### 1
num = 43
num = int(input("Enter an integer: ", ))
if num % 2 == 0:
    print("43 is an even number!")
else:
    print("43 is an odd number!")
    
#### 2
num = 32
num = int(input("Enter an integer: ", ))
if num % 2 == 0:
    print("32 is an even number!")
else:
    print("32 is an odd number!")

### :heavy_plus_sign: Task 4 - circle area

### Your task is to write a Python program which accepts (prompts) the **float** radius of a circle from the user and compute its 
### [area](https://www.mathsisfun.com/geometry/circle-area.html).  
### Round the result to two decimals!  
### Print out an appropriate message to the user.
#### >Hint: You can import `pi` number from `math` module for convenience!

radius = 3.45
area = 37.39
from math import pi
radius = float(input("Enter the radius of circle : "))
unit = input("Enter the measure unit of radius (e.g. in, cm) : ")
# area = pi * (r*r)
area = round(pi * 3.45 * 3.45, 2)
print("The area of the circle is: ", area, unit+"2")

### :heavy_plus_sign: Task 5 - guess a number
### Your task is to write a Python program to guess a number between 1 to 10.
### >Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
# on successful guess, user will get a "Well guessed!" message, and the program will exit.
### >Hint: you don't know the `random` module yet, so set your number to guess hard-coded in your program. 

#### Option 1
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input("Guess a number between 1 and 10 until you get it right:", ))
print('Well guessed!')

#### Option 2
from random import randint as rt
guess_num = rt(1,9)

while True:
    user_guess = int(input("Guess a number between 1 and 10 until you get it right: ", ))
    if guess_num == user_guess:
        print("Well guessed!")
        break
    else:
        print("Incorrect!\n")
        
#### Option 3 (Solution by Jaman)
target_number = 7
guess_number = int(input("Guess a number between 1 and 10 until you get it right: ", ))
while guess_number != target_number:
    print("Well guessed!")
    break

### :heavy_plus_sign: Task 6 - Celsius to Fahrenheit conversion
### Your task is to write a Python program to convert temperatures to and from Celsius, Fahrenheit.
### In the centigrade scale, which is also called the Celsius scale, water freezes at 0 degrees and boils at 100 degrees.  
### In the Fahrenheit scale, water freezes at 32 degrees and boils at 212 degrees. 
### Note : User should be prompted twice:  
 #- to enter a temperature,  
 #- to enter a shortcut for given scale (C for Celsius, F for Fahrenheit).
### > Formula : C/5 = F-32/9, where C = temperature in Celsius and F = temperature in Fahrenheit.

#### OPTION 1
Temperature = input("Enter type of Temperature you want to convert (C: Celsius F: Fahrenheit): ", )
value = float(input("Enter the value of Temperature to be converted: ", ))
if Temperature == "C":
    print("Temperature in Fahrenheit: ", round((value * 1.8) + 32, 0))
elif Temperature == "F":
       print("Temperature in Celsius: ", round((value - 32) * (0.56), 0))

#### OPTION 2
    # Celsius to Fahrenheit
input("Enter C for converting Celsius to Fahrenheit: ", )
celsius = float(input("Enter the Temperature in Celsius to be converted: ", ))
fahrenheit = (1.8 * celsius) + 32
print("Temperature in Fahrenheit: ", fahrenheit)
    # Fahrenheit to Celsius
input("Enter F for converting Fahrenheit to Celsius: ", )
fahrenheit = float(input("Enter the Temperature in Fahrenheit: ", ))
celsius = (fahrenheit - 32) * (0.56)
print("Temperature in Celsius: ", celsius)

### :heavy_plus_sign: Task 7 - pattern
### Your task is to write a Python program to construct the following pattern. Upper part should be done **in one line** of code without using a loop.  
### Lower part can be done with any kind of loop **or** also with one line of code and without loops.

### TASK 7
print('* ', 2 * '* ', 3 * '* ', 4 * '* ', 5 * '* ', sep='\n')
for i in range (4, 0, -1):
    print(i * '* ')
    

### :heavy_plus_sign: Task 8 - Fibonacci series
### Your task is to write a Python program to get the Fibonacci series between 0 to 50.  
### >Note: The Fibonacci Sequence is the series of numbers :
### 0, 1, 1, 2, 3, 5, 8, 13, 21, ....  
### Every next number is found by adding up the two numbers before it. 

#### TASK 8
#### Option 1
num1 = 0
num2 = 1
num = int(input("Enter the maximum value of sequence: ", ))
while num <= 50:
    print("Fibonacci Sequence from 0 to 50 is: ", )
    print(num1, num2, end=" ")
    for i in range(2, 10):
        num1, num2 = num2, num1 + num2
        print(num2, end=" ")
    break

#### Option 2
