# Day 1 Problem 2
file = open("/home/nullasec/Desktop/AdventOfCode/2024/Day1.txt", "r")

numList = file.read()

list1 = []
list2 = []

lines = numList.strip().split("\n")

for line in lines:
    col1, col2 = line.split()

    list1.append(int(col1))
    list2.append(int(col2))

total = 0

for i in list1:
    occurences = 0

    for j in list2:
        if i == j:
            occurences += 1

    i *= occurences
    total += i


print (total)