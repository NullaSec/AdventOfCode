# Day 1 Problem 1
file = open("/home/nullasec/Desktop/AdventOfCode/2024/Day1.txt", "r")

numList = file.read()

list1 = []
list2 = []

lines = numList.strip().split("\n")

for line in lines:
    col1, col2 = line.split()

    list1.append(int(col1))
    list2.append(int(col2))

list1.sort()
list2.sort()

counter = 0
for i,j in zip(list1, list2):
    counter += abs(i-j)

print(counter)