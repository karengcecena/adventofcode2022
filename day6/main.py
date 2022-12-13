input = open("input.txt").read()
ex = open("ex.txt").read()

"""
part 1
"""

# start = 0
# end = 4

# for ex: 
# for i in range(len(ex)-4):
#     marker = ex[start:end]
    
#     if len(marker) == len(set(marker)):
#         print(end)
#         break

#     start += 1
#     end += 1

# for input
# for i in range(len(input)-4):
#     marker = input[start:end]
    
#     if len(marker) == len(set(marker)):
#         print(end)
#         break

#     start += 1
#     end += 1

"""
part 2
"""
# A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.

start = 0
end = 14

# for ex: 
# for i in range(len(ex)-14):
#     marker = ex[start:end]
    
#     if len(marker) == len(set(marker)):
#         print(end)
#         break

#     start += 1
#     end += 1

# for input
for i in range(len(input)-14):
    marker = input[start:end]
    
    if len(marker) == len(set(marker)):
        print(end)
        break

    start += 1
    end += 1