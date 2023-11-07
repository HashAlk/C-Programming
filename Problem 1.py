#Rajveer made this one but i assisted 
#name: Hashim
#Date: November 6th 2023
#Problem: 1
name=input("what is your name ")
contnum =-1
print(f"hello {name} its nice to meet you")
totalnum=0
continents=["asia","europe","north america","south america","australia", "africa","antartica"]
for continent in continents:
    contnum +=1
    contQ=input(f"have you been to {continents[contnum]} ")
    if contQ.lower()=="yes":
        totalnum +=1
print(f"you have visited {totalnum}/7 continents")