# ####
# 1. Create a simple calculator in Python.
# 2. The calculator should be able to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
# 3. The user should be able to input two numbers and choose the operation they want to perform.
# 4. The calculator should display the result of the calculation.
# 5. You can add extra features like performing square root, percentage, etc.
# This project will cover the following areas of PCEP (Python Certified Entry-Level Programmer):
# * Input and Output
# * Data Types
# * Variables
# * Operators
# * Conditional statements
# * Loops
# The project will help you strengthen your understanding of basic concepts in Python and also improve your problem-solving skill
import math
print("Welcome to the calculator")
while True:
    opreator = input("what is youre opreation")
    if opreator == "√": 
        squar_root=input("what number do you wnat to preform the square root operator on")
        print (math.sqrt(squar_root))
    else:
        number_1 =int(input("what is youre first nuber"))
        number_2 =int( input("what is youre second nuber"))
        if number_1 or number_2 < 0 :
             raise ValueError ("sory we dont suport negative numbers please enter a postive number")
           
        elif opreator == "+" :
             print(number_1 + number_2)
        elif opreator == "*":
            print(number_1 * number_2)
        elif opreator == "/":
            print(number_1 / number_2)
        elif opreator == "%":
             print(number_1 / number_2 * 100)
        else:
               raise ValueError("sory the opreator you entered is invalid")
 
