# Chatbot 
# Author: Hashim Alkhatab
# Date 21 September 2023
import time
print("Hello my name is CHATBOT in order for me to know you better please fill out these question!")
time.sleep(1)
name = input("My name is: ")
time.sleep(0.3)
favorite_sport = input("My favorite sport is: ")
time.sleep(0.3)
favorite_food = input("My favorite food is: ")
time.sleep(0.3)
favorite_class = input("Whats your favorite class: ")
game_choice = input("Thanks for sharing this information to me now that i know you better do you want to play a game? ")
if game_choice.capitalize() ==  ("yes"):
    print("YAYYY ")
