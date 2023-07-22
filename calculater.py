# calculater app
import math
def addition(num1 , num2):
   print(num1 + num2)

def substraction(num1 , num2):
   print(num1 - num2)

def multiplycation(num1 , num2):
   print(num1 * num2)

def divtion(num1 , num2):
      print(num1 / num2)

def factorial(factoril):
   print(math.factorial(factoril))


print('Welcome to the calculater app')
while True:
  choice = input("which feature do you want \n A: addition B: substraction C: multiplycation d: division E: factorial , Q: exit")
  choice = choice.upper()
  if choice == 'A':
   try:
      num1 = int(input("Please pick youre first number to add: "))
      num2 = int(input("Please pick youre second number to add: "))
      addition(num1 , num2)
   except ValueError:
      print('Please add a valid number')

  elif choice == 'B':
   try:
      num1 = int(input("Please pick youre first number to substract: "))
      num2 = int(input("Please pick youre second number to substract: "))
      substraction(num1 , num2)

   except ValueError:
      print('Please add a valid number')


  elif choice == 'C':
   try:
      num1 = int(input("Please pick youre first number to multiply: "))
      num2 = int(input("Please pick youre second number to multiply: "))
      multiplycation(num1 , num2)
   except ValueError:
      print('Please add a valid number')

  elif choice == 'D':
   try:
      num1 = int(input("Please pick youre first number to divid: "))
      num2 = int(input("Please pick youre second number to divid: "))
      divtion(num1 , num2)
   except ValueError:
      print('Please add a valid number') 
    
   except ZeroDivisionError:
      print('ZeroDivisionError')


  elif choice == 'E':
   try:
      factorial_num = int(input("Please pick youre number to find its factorial: "))
      factorial(factorial_num)
   except ValueError:
      print('Please add a valid number') 
  elif choice == "Q":
     break

  else:
   print("the feature you added is curntly not avalible please inform it to us and we will add it as sone as possible") 




   

