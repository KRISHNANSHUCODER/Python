n = int(input("Enter the limit--> "))
a = 0; b = 1
print(a, b, end = " ")
for i in range(n+1):
    c = a+b
    a = b
    b = c
    print(c, end =" ")
