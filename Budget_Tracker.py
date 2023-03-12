output_file = open("extension.bin", "w", encoding="UTF-8")


Rent=float(input("What is youre Rent:"))
Utilities=float(input("What is youre Utilities amount"))
Groceries=float(input("What is youre Groceries amount"))
Transportation=float(input("What is youre Transportation amount"))
Entertainment=float(input("What is youre Entertainment amount"))
list_of_expnses={"Rent": Rent,
                "Utilities":Utilities,
                "Groceries":Groceries,
                "Transportation":Transportation,
                "Entertainment":Entertainment,
                # List of erxpnses
}
if Rent > 0 : 
    raise ValueError ("you cant use negative number") # eror checking for the list

elif Utilities > 0 :
   raise ValueError ("you cant use negative number") 

elif Groceries > 0 :
   raise ValueError ("you cant use negative number") 
elif Transportation > 0 :
   raise ValueError ("you cant use negative number") 
elif Entertainment > 0 :
   raise ValueError ("you cant use negative number") 
source_of_income=int(input("How many sorces of income do you have? "))

list_of_income={} 

for income in range (0 , source_of_income):
    income = income + 1 # That is the loop that is incharge of giving us the expnses and income 
    job="What is youre" ,  income , "source of income"
    user=input(job)
    monthly_wage="How much do you earn on youre " , income , " source of income" 
    monthly_wage_1=int(input(monthly_wage))
    if monthly_wage_1 > 0 :
            raise ValueError("You cannot enter a a value that is negtive")

    list_of_income[user] = monthly_wage_1
total_expnse = Rent + Utilities + Groceries + Transportation + Entertainment
print(list_of_expnses, file=output_file)
print(list_of_income, file=output_file)
output_file.close()

print(list_of_expnses)
print(list_of_income)
budget=int(input("what is youre total budget"))
print("Your total expenses are", total_expnse, "and your budget is", budget) 
if budget==total_expnse:
  print("Youre budget is equal to expnses")

elif budget > total_expnse:
  print("Youre budget is fewer then expnses")

elif budget < total_expnse:
  print("Youre budget is greater then total expnses")

elif total_expnse == 0:
    raise ValueError("You cannot enter a a value that is equal to zero")
elif total_expnse < 0:
       raise ValueError("Total expnses cannot be a  negative  number")
