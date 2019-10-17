'''ThoughtWorks 2020'''


n = int(input())
a = list(map(int, input().split(' '))) #take mutliple input in same line as a list
print("you give: ", a)
l_old = []
l_new = []
l_old = a
print("the old value: ", l_old) #keep the old values of a


l_new = sorted(a) #l_new contain the sorted list
print("the new value: ", l_new) #a is now sorted and updated as list is mutable

good = 0
bad = 0
for i in range(len(a)):
    if l_old[i] == l_new[i]:
            good += l_old[i]
    else:
            bad += l_old[i]
num = good - bad
print(good)
print(bad)
print(num)




