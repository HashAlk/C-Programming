#This gives a list of names and the ages of those names.
names = [["Hashim", 14], ["Drew", 14], ["Marcus", 7]]

#This acsesses the lists inside the "MAIN" list.
for name in names:
    number = len(name)
    if number == 0:
        print(name, "is", end=(" "))
    else:
        print(name, end=(" "))
print("\n")
# for name in names:
#     for index in name:
#         if index == 0:
#             print(index,"is", end=(" "))
#         else:
#             print(index, end=(" "))
#     print("\n")
        

