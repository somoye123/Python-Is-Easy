# I/O using python built in input and print keywords
Var = input("Message to the user")

Name = input("Please enter your name: ")
print(Name)

Age = int(input("Please enter your age: "))
# print(int(Age) +1)

Scores = []

for i in range(5):
    currrentScore = float(input("Please enter the score "+ str(i+1)))
    Scores.append(currrentScore)
    print("The score you entered was:\n"+str(currrentScore))
print(Scores)

# I/0 with file system
# File = open("Filename","r") # "r", "w", "a", "r+"

VacationSpots = ["London","Paris","New York","Utah","Iceland"]

VacationFile = open("VacationPlaces","w")

for Spots in VacationSpots:
    VacationFile.write(Spots + "\n")

VacationFile.close()

VacationFile = open("VacationPlaces", "r")

for line in VacationFile:
    print(line, end="")

VacationFile.close()
# TheWholeFile = VacationFile.read()
# print(TheWholeFile)

FinalSpot = "Thailan\n"

VacationFile = open("VacationPlaces","a")
VacationFile.write(FinalSpot)
VacationFile.close()

VacationFile = open("VacationPlaces", "r")

for line in VacationFile:
    print(line, end="")

VacationFile.close()

for i in range(5):
    # the with keyword helps to automatically close the file
    with open("VacationPlaces"+str(i),"r") as VacationFile:
        for line in VacationFile:
            print(line)
            