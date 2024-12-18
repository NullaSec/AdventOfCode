# Day 2 Problem 1
file = open("/home/nullasec/Desktop/AdventOfCode/2024/Day2.txt", "r")

levels = file.read()
lines = levels.strip().split("\n")

def is_safe(report):
    lvlList_int = [int(x) for x in report.split()]

    is_increasing = all(lvlList_int[i] < lvlList_int[i+1] for i in range(len(lvlList_int)-1))
    is_decreasing = all(lvlList_int[i] > lvlList_int[i+1] for i in range(len(lvlList_int)-1))

    if not (is_increasing or is_decreasing):
        return False
    
    return all(1 <= abs(lvlList_int[i] - lvlList_int[i+1]) <= 3 for i in range(len(lvlList_int)-1))

safe_counter = sum(1 for line in lines if is_safe(line))

print(safe_counter)


        
            
            
