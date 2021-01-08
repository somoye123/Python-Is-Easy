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