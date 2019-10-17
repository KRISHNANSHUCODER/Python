l = []
l = input().split()
l = [int(i) for i in l]
print(l)
list = list(filter(lambda x:(x%3 != 0), l))
print(list)
for i in list:
    print(i,end=" ")