rucksacks = open("input.txt").readlines()
ex = open("ex.txt").readlines()

alphabet_dict = {}

ALPHABET_dict = {}

alphabet_dict_complete = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                        'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 
                        'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 
                        'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

# # set sum of priority numbers to zero
# sum = 0

# # loop through each line in the txt file 
# for line in rucksacks:
#     # take off the break line from the line
#     line = line.strip("\n")
#     # get the middle index of that line and... 
#     mid = len(line)//2
#     # print("middle index:", mid)

#     # ... split the compartments into 2 equal compartments
#     first_compartment = set(line[:mid])
#     # print("first compartment:", first_compartment, len(first_compartment))

#     second_compartment = set(line[mid:])
#     # print("second compartment:", second_compartment, len(second_compartment))

#     # create a list, from the set math used to get the only matching character
#     priority_letter_list = list(first_compartment & second_compartment)
#     # use that list to index into it so you can get that character
#     priority_letter = priority_letter_list[0]
#     # print(priority_letter)

#     # use the alphabet to get that letters value to sum it all up
#     sum += alphabet_dict_complete[priority_letter]

# # print the final sum
# print(sum)

"""
Part 2
"""

# set sum of priority numbers to zero
sum = 0

# keep track of groups of lines 
line_num = 1
current_lines = []

# loop through each line in the txt file 
for line in rucksacks:
    # take off the break line from the line
    line = line.strip("\n")

    # when the count is less then 4 == every three lines
    if line_num < 4: 
        # add that to the current lines we are looking at
        current_lines.append(line)
        # increase the count
        line_num += 1
    
    # after you have gone through 3 lines
    else: 
        # check what the badge letter it by using set math of each rucksack
        badge = list(set(current_lines[0]) & set(current_lines[1]) & set(current_lines[2]))
        # add the value of the badge to the sum
        sum += alphabet_dict_complete[badge[0]]

        # reset current lines to include the current line we are on because it is basically getting skipped in the else statement
        current_lines = [line]
        # set line_num to 2 because it was skipped so we have to add 1 to what we had originally as a start
        line_num = 2

# for the last three in the current_lines folder
if current_lines: 
    # check what the badge letter it by using set math of each rucksack for the last three lines
    badge = list(set(current_lines[0]) & set(current_lines[1]) & set(current_lines[2]))
    # add the value of the badge to the sum
    sum += alphabet_dict_complete[badge[0]]

# print the final sum
print(sum)

"""
CODE TO CREATE THE DICTIONARIES MORE EASILY
"""

# alph_count = 1

# for char in "abcdefghijklmnopqrstuvwxyz":
#     alphabet_dict[char] = alph_count
#     alph_count += 1

# ALPH_count = 27

# for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#     ALPHABET_dict[char] = ALPH_count
#     ALPH_count += 1

# print(alphabet_dict)
# print(ALPHABET_dict)
