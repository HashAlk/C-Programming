import turtle
TURTLE_MAGNITUDE = 20
#create a turtle
michealangelo = turtle.Turtle()

#get some intructions from the user
print("""to give commands, type:
W - to go forward
A - to go left
D - to go right
S - to go backward
STOP - to stop the code""")

while True:
    command = input(" ")
    if command.strip("?.!:', ").lower() == "stop":
        break
    elif command.strip("?.!:', ").lower() == "w":
        michealangelo.forward(TURTLE_MAGNITUDE)
    elif command.strip("?.!:', ").lower() == "s":
        michealangelo.forward(TURTLE_MAGNITUDE - 25)
    elif command.strip("?.!:', ").lower() == "a":
        michealangelo.left(90)
    elif command.strip("?.!:', ").lower() == "d":
        michealangelo.right(90)
turtle.done()