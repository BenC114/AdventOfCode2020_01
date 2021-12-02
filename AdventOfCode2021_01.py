'''
Created on Sep 1, 2021

@author: bculv
'''

print("Hello World")

#Initializing arrays and opening the files
dict_array=[]
dict_file = open("C:/Users/bculv/Documents/VS Code/nums.txt","r") 
dict_file2 = open("C:/Users/bculv/Documents/VS Code/nums.txt")

#Read the file in and put it into array
for line in dict_file:
    dict_array.append(line.rstrip('\n'))
print(dict_array)

#Problem 1
previousI = 0
currentI = 1
counter = 0
num = 1
for num in range(len(dict_array)):
    previousI = int(dict_array[num - 1])
    currentI = int(dict_array[num])
    if currentI > previousI:
        counter+=1
print(counter)

#Problem 2
dict_array2 = []
counter = 0

#Reading in the numbers into an array
for line in dict_file2:
    dict_array2.append(line.rstrip('\n'))
print (dict_array2)

#Initializing Variables
startPointer = 0
endPointer = 2
sumCounter = 0
previousSum = 0
currentSum = 0
increaseCounter = 0

#While the statPointer stays in range, continue looping
while startPointer + 3 < len(dict_array2):
    
    #Only needed on first iteration because we set previousSum = currentSum
    if previousSum == 0:
        while sumCounter < 3:
            previousSum = previousSum + int(dict_array2[startPointer + sumCounter])
            sumCounter += 1
    startPointer += 1
    endPointer += 1
    sumCounter = 0
    
    #Calculate currentSum every iteration
    while sumCounter < 3:
        currentSum = currentSum + int(dict_array2[startPointer + sumCounter])
        sumCounter += 1
    
    #Determine if increase or not
    if (currentSum > previousSum):
            increaseCounter += 1
    
    #Reset variables to acceptable values
    previousSum = currentSum
    currentSum = 0
print(increaseCounter)
    
    