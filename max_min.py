import numpy as np
list = []
list = input().split() #take input in same line
print(list)
list = [int(x) for x in list] # create list as int
list.sort()
print(list)
print(max(list), min(list)) # max() no in list and min() no in list