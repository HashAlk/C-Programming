#AOC Day 1
#Author: Hashim Al-Khatab
#30th november 2023

#There is one elf caryying the most calories
#How many does that one have?
elves = []
#open the file
with open("./aoc2022day1.txt") as f:
#current CALORIES of the current elf
    current_cals = 0
    for line in f:
        #if there is something in the line this is going to return TRUE
        if line.strip():
            current_cals += int(line.strip())
        else:  
            #dump current cals into elves list
            elves.append(current_cals)
            #reset current_cals for next elf
            current_cals = 0
biggest_cals = 0

for elf in elves:
    if elf > biggest_cals:
        biggest_cals = elf
print(biggest_cals)