# Day 1 - Calorie Count

with open('calories_day1.txt') as calories_file:
    calories = [i for i in calories_file.read().strip().split("\n")]

calories_max = 0
calories_count = 0
max2 = 0
max3 = 0
for element in calories:
    if element == '':
        calories_count = 0
    else:
        current_num = int(element)
        calories_count += current_num

    if calories_count > calories_max:
        max3 = max2
        max2 = calories_max
        calories_max = calories_count
    elif calories_count > max2:
        max3 = max2
        max2 = calories_count
    elif calories_count > max3:
        max3 = calories_count

print(f"The Elf is carrying {calories_max} calories")  # Part 1
print(f"In total, the Elves carrying {calories_max + max2 + max3} calories.")  # Part 2
