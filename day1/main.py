
# opening the file, and reading it as strings made by each line
# readlines() = Reads all the lines and return them as each line a string element in a list
elves_file = open("input.txt").readlines()

# create a list of all the sums of each elf chunk of lines
calorie_total_lst = []

# to keep track of each elves calories
counter = 0

# go through each line in the file
for n in elves_file:
    # if you take away the \n from the string file that was made, and there is still stuff (aka the numbers and not an empty line)
    if n.strip("\n"):
        # make the string n to an integer n 
        n = int(n.strip("\n"))
        # add that n to the counter
        counter += n
    # if you encounter an empty line
    else:
        # add the current counter total to the list for that elves total calories
        calorie_total_lst.append(counter)
        # reset the counter to zero for the next elf
        counter = 0

# print out the max number in that list to get the elf with the most calories
print(max(calorie_total_lst))

# sort calorie count from smallest to greatest
calories_sorted = sorted(calorie_total_lst)

# get the last three calorie amounts by negative indexing (these are the biggest calorie amounts) and add them
top_three = calories_sorted[-1] + calories_sorted[-2] + calories_sorted[-3]
# print that top_three number to know what it is 
print(top_three)

# double checking by just grabbing those three numbers in that list and adding them
# print(68164 + 69894 + 70509)
