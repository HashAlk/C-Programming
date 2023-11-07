#Hashim Alkhatab
#Date: November 6th 2023
#Question 3:
#Asks the user if they would like burgers and fries and stores the answer
burger=input("would you like a burger for 5$ (yes/no) ")
fries=input("would you like fries for 3$ (yes/no) ")
totalCost=0
#if the user said yes for the bigger it will add the cost to the totalcost.
if burger.lower()== "yes":
    totalCost+=5
#if the user said yes for the fries it will add the cost to the totalcost.
if fries.lower()=="yes":
    totalCost+=3
#this multiples the total cost by 0.14 to add the the expense of tax.
tax=totalCost* 0.14
#prints the finaltotalcost.
print(f"${tax+ totalCost}")