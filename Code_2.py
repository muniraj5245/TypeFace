str1=input()
str2=input()
x=str2[len(str2)-1]
count=0
for i in str1:
  if i==x:
    count+=1
print(count)