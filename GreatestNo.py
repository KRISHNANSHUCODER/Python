'''
first we have to take input in a line using .split(' ') seperated by space
map to take all input map(data type, input())
list to take all mapped input in a list using function list()
'''

m = list(map(int, input("Enter a multiple value: ").split(' '))) #take multiple integer input in a line
p = len(m)
if(p==10):
    print("The max value is:",max(m))
else:
   print("Insufficient input must need",p,"integers")
