n = input().split()# take input sepetarely#
print(n)
b = n[0]#1st element of input#
c = n[-1]#last element of input#
b = int(b)
c = int(c)
print(b)#prinr 1st element#
print(c)#print 2nd element#
for a in range(int(n[-1])):
    print(n[a])
i = 0
l = []
for i in range(b,c+1):
    l.append(i)
    print(l)
