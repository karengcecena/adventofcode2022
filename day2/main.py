# open the file 
actions = open("input.txt").readlines()

# open example file to make sure the algorithm works correctly
ex_actions = open("ex.txt").readlines()

# start with a score of zero 
score = 0

"""
first version
"""

# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# The score for a single round is the score for the shape you selected 
    # (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round 
    # (0 if you lost, 3 if the round was a draw, and 6 if you won).

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

#####################################################################

# # loop through each line 
# for line in actions: 
#     # A = Rock
#     if line[0] == "A":
#         # X = Rock, tie
#         if line[2] == "X":
#             score += 4
#         # Y = Paper, win
#         elif line[2] == "Y":
#             score += 8 
#         # Z = Scissors, lost
#         elif line[2] == "Z":
#             score += 3
#     # B = Paper
#     elif line[0] == "B":
#         # X = Rock, lost
#         if line[2] == "X":
#             score += 1
#         # Y = Paper, tie
#         elif line[2] == "Y":
#             score += 5 
#         # Z = Scissors, win
#         elif line[2] == "Z":
#             score += 9
#     # C = Scissors
#     elif line[0] == "C": 
#         # X = Rock, win
#         if line[2] == "X":
#             score += 7
#         # Y = Paper, lost
#         elif line[2] == "Y":
#             score += 2 
#         # Z = Scissors, tie
#         elif line[2] == "Z":
#             score += 6

# print(score)

"""
second version
"""

# "Anyway, the second column says how the round needs to end: 
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win. Good luck!"

#####################################################################

for line in actions: 
    # A = Rock
    if line[0] == "A":
        # X = lose, scissors
        if line[2] == "X":
            score += 3
        # Y = tie, rock
        elif line[2] == "Y":
            score += 4
        # Z = win, paper
        elif line[2] == "Z":
            score += 8
    # B = Paper
    elif line[0] == "B":
        # X = lose, rock
        if line[2] == "X":
            score += 1
        # Y = tie, paper
        elif line[2] == "Y":
            score += 5
        # Z = win, scissors
        elif line[2] == "Z":
            score += 9
    # C = Scissors
    elif line[0] == "C": 
        # X = lose, paper
        if line[2] == "X":
            score += 2
        # Y = tie, scissors
        elif line[2] == "Y":
            score += 6
        # Z = win, rock
        elif line[2] == "Z":
            score += 7

print(score)