ex = open("ex.txt").readlines()
input = open("input.txt").readlines()

# start a counter
counter = 0

### check if the ranges are COMPLETELY WITHIN the other range

# # go through every line
# for line in input: 
#     # strip the lines of the \n
#     line = line.strip("\n")
#     # get the two sets of ranges
#     first_range, second_range = line.split(",")

#     # get the first and last number of the first range
#     first_num_first_range, second_num_first_range = first_range.split("-")

#     # get the first and last number of the second range
#     first_num_second_range, second_num_second_range = second_range.split("-")

#     # check if either ranges contain both of the other ranges numbers
#     if int(first_num_first_range) in range(int(first_num_second_range), int(second_num_second_range) + 1) and int(second_num_first_range) in range(int(first_num_second_range), int(second_num_second_range) + 1) or int(first_num_second_range) in range(int(first_num_first_range), int(second_num_first_range) + 1) and int(second_num_second_range) in range(int(first_num_first_range), int(second_num_first_range) + 1):
#         # if they do, add 1 to the counter
#         counter += 1

# # print the counter to know the total number
# print(counter) 

"""
part 2
"""
### check if the ranges are SOMEWHAT WITHIN the other range

# # go through every line
# for line in input: 
#     # strip the lines of the \n
#     line = line.strip("\n")
#     # get the two sets of ranges
#     first_range, second_range = line.split(",")

#     # get the first and last number of the first range
#     first_num_first_range, second_num_first_range = first_range.split("-")

#     # get the first and last number of the second range
#     first_num_second_range, second_num_second_range = second_range.split("-")

#     # check if either ranges contain either of the other ranges numbers
#     if int(first_num_first_range) in range(int(first_num_second_range), int(second_num_second_range) + 1) or int(second_num_first_range) in range(int(first_num_second_range), int(second_num_second_range) + 1) or int(first_num_second_range) in range(int(first_num_first_range), int(second_num_first_range) + 1) or int(second_num_second_range) in range(int(first_num_first_range), int(second_num_first_range) + 1):
#         # if they do, add 1 to the counter
#         counter += 1

# # print the counter to know the total number
# print(counter) 

"""
fixing my code
"""
# """ 
# trying to make my code better
# didn't work 
# """

# # go through every line
# for line in input: 
#     # stip the lines of the \n
#     line = line.strip("\n")
#     # get the two sets of ranges
#     first_range, second_range = line.split(",")

#     # get the first and last number of the first range
#     first_num_first_range, second_num_first_range = first_range.split("-")

#     # get the first and last number of the second range
#     first_num_second_range, second_num_second_range = second_range.split("-")

#     # make the string numbers above integer type
#     first_num_first_range, second_num_first_range = int(first_num_first_range), int(second_num_first_range)
#     first_num_second_range, second_num_second_range = int(first_num_second_range), int(second_num_second_range)

#     # check if either ranges contain both of the other ranges numbers
#     if first_num_first_range in range(first_num_second_range, second_num_second_range+ 1):
#         if second_num_first_range in range(first_num_second_range, second_num_second_range + 1): 
#             # if they do, add 1 to the counter
#             counter += 1
        
#     if first_num_second_range in range(first_num_first_range, second_num_first_range + 1):
#         if second_num_second_range in range(first_num_first_range, second_num_first_range + 1):
#             # if they do, add 1 to the counter
#             counter += 1

# # print the counter to know the total number
# print(counter) 