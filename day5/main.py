"""
example: 
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
input.txt: 

[T]     [Q]             [S]        
[R]     [M]             [L] [V] [G]
[D] [V] [V]             [Q] [N] [C]
[H] [T] [S] [C]         [V] [D] [Z]
[Q] [J] [D] [M]     [Z] [C] [M] [F]
[N] [B] [H] [N] [B] [W] [N] [J] [M]
[P] [G] [R] [Z] [Z] [C] [Z] [G] [P]
[B] [W] [N] [P] [D] [V] [G] [L] [T]
 1   2   3   4   5   6   7   8   9 
 """

ex = open("ex.txt").readlines()
input = open("input.txt").readlines()

"""
part 1
"""
### make own stacks/ queues in dictionaries because easier to access through concatenation of input strings and original name: 

# example stacks / queues
examples = {
    "ex1" : ["Z", "N"],
    "ex2" : ["M", "C", "D"],
    "ex3" : ["P"]
}

# input stacks / queues
inputs = {
    "input1" : ["B", "P", "N", "Q", "H", "D", "R", "T"],
    "input2" : ["W", "G", "B", "J", "T", "V"],
    "input3" : ["N", "R", "H", "D", "S", "V", "M", "Q"],
    "input4" : ["P", "Z", "N", "M", "C"],
    "input5" : ["D", "Z", "B"],
    "input6" : ["V", "C", "W", "Z"],
    "input7" : ["G", "Z", "N", "C", "V", "Q", "L", "S"],
    "input8" : ["L", "G", "J", "M", "D", "N", "V"],
    "input9" : ["T", "P", "M", "F", "Z", "C", "G"]
}

# AS STACKS 

# # for examples
# for line in ex:
#     line = line.strip("\n")
#     line = word_move, amount, word_from, origin, word_to, destination = line.split(" ")

#     for i in range(int(amount)):
#         origin_list = ("ex" + origin)
#         destination_list = ("ex" + destination)

#         letter = examples[origin_list].pop()
#         examples[destination_list].append(letter)

# print("Stacks:")
# print(examples["ex1"][-1] + examples["ex2"][-1] + examples["ex3"][-1])

# # for input
# for line in input:
#     line = line.strip("\n")
#     line = word_move, amount, word_from, origin, word_to, destination = line.split(" ")

#     for i in range(int(amount)):
#         origin_list = ("input" + origin)
#         destination_list = ("input" + destination)

#         letter = inputs[origin_list].pop()
#         inputs[destination_list].append(letter)

# print("Stacks:")
# print(inputs["input1"][-1] + inputs["input2"][-1] + inputs["input3"][-1] + inputs["input4"][-1]+ inputs["input5"][-1] + inputs["input6"][-1] + inputs["input7"][-1] + inputs["input8"][-1] + inputs["input9"][-1])

"""
part 2
"""

# AS QUEUES/ STAY IN SAME ORDER

# for examples
for line in ex:
    line = line.strip("\n")
    line = word_move, amount, word_from, origin, word_to, destination = line.split(" ")

    origin_list = ("ex" + origin)
    destination_list = ("ex" + destination)

    letters = examples[origin_list][-int(amount):]

    for i in range(int(amount)):
        examples[origin_list].pop()

    examples[destination_list].extend(letters)

print("Stay in same order:")
print(examples["ex1"][-1] + examples["ex2"][-1] + examples["ex3"][-1])

# for input
for line in input:
    line = line.strip("\n")
    line = word_move, amount, word_from, origin, word_to, destination = line.split(" ")

    origin_list = ("input" + origin)
    destination_list = ("input" + destination)

    letters = inputs[origin_list][-int(amount):]

    for i in range(int(amount)):
        inputs[origin_list].pop()

    inputs[destination_list].extend(letters)

print("Stay in same order:")
print(inputs["input1"][-1] + inputs["input2"][-1] + inputs["input3"][-1] + inputs["input4"][-1]+ inputs["input5"][-1] + inputs["input6"][-1] + inputs["input7"][-1] + inputs["input8"][-1] + inputs["input9"][-1])
