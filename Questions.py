#Hashim Alkhatab
#Assignment: Questions 1-3
#Date: November 6th 2023



#Question 1:
#Asks the user how old they are.
age=int(input("how old are you? "))
#takes there age and addes 26.
finalAge= age + 26
#prints there age when they are in 2049.
print(f"you will be {finalAge} in 2049")



#Question 2:
#This asks the JUDGES to input there score.
judge_one = float(input("Please enter the score you see reasonable judge number 'ONE'"))
judge_two = float(input("Please enter the score you see reasonable judge number 'TWO'"))
judge_three = float(input("Please enter the score you see reasonable judge number 'THREE'"))
judge_four = float(input("Please enter the score you see reasonable judge number 'FOUR'"))
judge_five = float(input("Please enter the score you see reasonable judge number 'FIVE'"))
#this adds up the total score of all the judges.   
math = judge_one + judge_two + judge_three + judge_four + judge_five
#this checks if the total score is equal or greater then 50 and responds based on that.
if math >= 50:
    print(f"The judges have given a POSTIVE score of: {math}")
else:
    print(f"The judges have given a NEGATIVE score of: {math}")



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