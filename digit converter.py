D = input() #take input#
n = list(D) #convet it in list[]#
print(n)
a = n.count('1') #count no of 1 in input#
b = n.count('0') #count no of 0 in input#
print(a)#print no of 1#
print(b) #print no of 0#
if(a==1 or b==1):
    print("YES") #make all no same possible#
else:
    print("NO") #make all no same not possible#