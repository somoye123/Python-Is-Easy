Word = "Hello"

Letters = []

for w in Word:
    print(w)
    if w == "e":
        print("what a funny letter")
    Letters.append(w)
print(Letters)

Numbers = [1,2,3,4,5]

for i in Numbers:
    if i%2 ==1:
        print(i)

# range(start,stopping,steps)

# for num in range(4)
for num in range(-1,13,3):
    Numbers.append(num)
    print(num)

print(Numbers)

# while (condition):
#     Action
#     Action2
#     Action3

Counter = 1

Sum = 0

while (Counter <=100):
    Sum += Counter
    Counter += 1

print(Sum)

Index = 1

while (Index < len(Letters)):
    print(Index)
    print(Letters[Index])
    Index += 1

height = 5000
velocity = 50
time = 0

while(height>0):
    height -= velocity
    time += 1
print(height)
print(time)

Participants = ["Jen","Alex","Tina","Joe","Ben"]

position = 1

for name in Participants:
    if name == "Alex":
        print("About to break")
        break
    print("About to increment")
    position +=1

print(position)