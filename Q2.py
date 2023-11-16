#Author: Hashim Alkhatab
#Date: Nov 16th 2023
#Assignment: ParentalBot
total_score = 0
questions = ["Did you eat: ","Did you study: ","Did you do your laundry: ","Did you call your grandma: "]

for question in questions:
    answer = input(question)
    if answer == "yes":
        total_score += 1

if total_score == 0:
    print("I'm coming over.")
elif total_score <3:
    print("Ok.")
elif total_score >=3:
    print("Good!")



