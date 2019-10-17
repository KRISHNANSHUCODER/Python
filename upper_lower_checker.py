string=input()#Enter your statement
count1=0
count2=0
for i in string:
      if(i.isupper()):
            count2=count2+1
      elif(i.islower()):
            count1=count1+1
print(count2,count1)#print no of uppercase in your statement
#print(count1)#print no of lowercase in your statement