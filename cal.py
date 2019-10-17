def f(m):
    if m == 0:
      return(0)
    else:
      return(m+f(m-1))
print(f(5))