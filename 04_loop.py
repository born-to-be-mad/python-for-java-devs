# Loops

# 1) while
# 2) for I in range(value)
# 3) for I in range(start value, end value)
rows = 10
i = 1
star = 1

for i in range(1, rows):
    for star in range(i):
        print("*", sep=' ', end=' ')
    print()

import math

startNumber = 1
endNumber = 25
print("Square\t\t\t\t" + "Square Root\t\t\t\t" + "Cube Root\t\t\t\t")

while (startNumber < endNumber):
    square = startNumber ** 2
    sqRoot = math.sqrt(startNumber)
    cubeRoot = math.pow(startNumber, 1.0 / 3)
    print(str(square) + " \t\t\t\t " + str(sqRoot) + " \t\t\t\t " + str(cubeRoot))
    startNumber = startNumber + 1

'''
for i in range (startNumber,endNumber):
	square = i * i
	sqRoot = math.sqrt(i)
	cubeRoot = math.pow(i, 1.0/3)
	print (str (square) + " \t\t\t\t " + str (sqRoot) + " \t\t\t\t "+ str (cubeRoot))
'''

'''
for startNumber in range (endNumber):
	square = startNumber * startNumber
	sqRoot = math.sqrt(startNumber)
	cubeRoot = math.pow(startNumber, 1.0/3)
	print (str (square) + " \t\t\t\t " + str (sqRoot) + " \t\t\t\t "+ str (cubeRoot))
'''
