# Loop-Practice
# Author: Hashim Alkhatab

# Developing a list of grocries to refer back to!
groceries = ["Burger", "IceCream", "Nutella", "HotDog"]

# Do something for each thing in the list
#  example : hotdog!
#     ---
#  * hotdog!
#     ---

for item in groceries: 
    print(f"* {item}")
    print(" ---")
          
# Create a pyramid using a for loop

stars = ["*", "**", "***", "****", "*****"]

for row in stars: 
    print(f"{row}")

 # * Starts off at 10  
 # * Countdown every second amd print the second that it's at
 # * Instead of reaching zero it says "Happy New Year"
 # "Happy New Year!"

import time

countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "happy new year..."]

for seconds in countdown: 
    print(f"{seconds}")
    time.sleep(1)