"""
Structure of a python function

def FunctionName(Input):
    Action
    return Output
"""

def addOne(Number):
    Output = Number +1
    return Output

Var = 0
print(Var)
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(2.1+3.4)
print(Var2)
print(Var3)
print(Var4)

def addOneAddTwo(NumberOne, NumberTwo):
    Output = NumberOne + 1
    Output += NumberTwo +2
    return Output

sum = addOneAddTwo(Var2,Var3)

print(sum)