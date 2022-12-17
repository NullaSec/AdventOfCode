# Day 2 - Rock Paper Scissors

# A/X - Rock     (1 point)
# B/Y - Paper    (2 points)
# C/Z - Scissors (3 points)

# Win  (Z) - 6 points
# Draw (Y) - 3 points
# Lose (X) - 0 points

# Possible Combinations (Part 1):
# A X : 1 + 3 = 4
# A Y : 2 + 6 = 8
# A Z : 3 + 0 = 3
# B X : 1 + 0 = 1
# B Y : 2 + 3 = 5
# B Z : 3 + 6 = 9
# C X : 1 + 6 = 7
# C Y : 2 + 0 = 2
# C Z : 3 + 3 = 6

with open('strategy_day2.txt') as strategy_file:
    strategy = strategy_file.read().split("\n")

combinations = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
}

total = 0
for round in strategy:
    total += combinations[round]

print('My total score is: ', total)  # Answer Part 1

# Possible Real Combinations (Part 2):
# A X (Lose): 3 + 0 = 3
# A Y (Draw): 1 + 3 = 4
# A Z  (Win): 2 + 6 = 8
# B X (Lose): 1 + 0 = 1
# B Y (Draw): 2 + 3 = 5
# B Z  (Win): 3 + 6 = 9
# C X (Lose): 2 + 0 = 2
# C Y (Draw): 3 + 3 = 6
# C Z  (Win): 1 + 6 = 7

combinationsPT2 = {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}

totalPT2 = 0
for round in strategy:
    totalPT2 += combinationsPT2[round]

print('My real total score is: ', totalPT2)  # Answer Part 2
