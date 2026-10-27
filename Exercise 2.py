# Question 1: Arithmetic and Assignment Operators
x= int(input("Enter a number:  "))
y= int(input("Enter a number:  "))
# TODO: Add 3 to x using the += operator
x += 3
# TODO: Multiply y by 2 using the *= operator
y *= 2
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a=4
b=2
c=3
# TODO: Create a condition that checks if a is greater than b
if a > b:
  True
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2 ==0:
  True
# TODO: Create a condition that checks if c is less than or equal to a
if c <= a:
  True
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
Final_condition = (a>b) or (b % 2 == 0) and (c <= a)
# TODO: Print the value of 'final_condition'
print(Final_condition)
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
Score = int(input("Enter your test score:  "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
if Score >= 90 and Score<= 100:
  grade = "A"
elif Score >= 80:
  grade = "B"
elif Score >= 70:
  grade = "C"
elif Score >= 60:
  grade = "D"
else:
  grade = "F"
# TODO: Print the grade for the given score
print("Your grade is", grade)
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("please enter a number:   "))
num2 = int(input("please enter a number:   "))
# TODO: Ask the user to input an operation  and store it in a variable called 'operation'
operation = input("Please enter and operation(+, -, *, /): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
if operation == "+":
  result = (num1 + num2)
elif operation == "-":
  result = (num1 - num2)
elif operation == "*":
  result = (num1 * num2) 
elif operation == "/":
  result = (num1 / num2) 
else:
  result = "Invalid Input"
# TODO: Handle the case of division by zero
if num2 == 0 and operation == "/":
  result = "invalid"

# TODO: Print the result of the operation
print(result)