"""
Structure of If Statements in Python

if condition:
    Action
"""

click = True

like = 0

if click == True:
    like += 1

print(like)

Temperature = 15
Thermo = 25

if Temperature <= 15:
    Thermo += 5

print(Thermo)

Time = 'Day'
Sleepy = False
Pajamax = 'off'
InBed = True

if Time == 'Night' or Sleepy == True:
    Pajamax = 'On'
elif Time == 'Morning' and InBed == True:
    Pajamax = 'On'
else:
    Pajamax = 'Off'

print(Pajamax)