from itertools import permutations
lst=[0,1,2,5,6,8,9]
perm=permutations(lst,2)
perm1=permutations(lst,3)
perm2=permutations(lst,4)
perm3=permutations(lst,5)
a=list(perm)+list(perm1)
b=list(perm2)+list(perm3)
c=a+b
lst1=[11,22,55,66,88,99,111,222,555,666,888,999,2222,5555,6666,8888,9999,11111,22222,55555,66666,88888,99999]
for i in c:
  if len(i)==2:
    (x,y)=i
    lst1.append(int(str(x)+str(y)))
  if len(i)==3:
    (x,y,z)=i
    lst1.append(int(str(x)+str(y)+str(z)))
  if len(i)==4:
    (x,y,z,a)=i
    lst1.append(int(str(x)+str(y)+str(z)+str(a)))
  if len(i)==5:
    (x,y,z,a,b)=i
    lst1.append(int(str(x)+str(y)+str(z)+str(a)+str(b)))
lst1.sort()
res=[*set(lst1)]
res=sorted(res)
n=int(input())
print(res[n-1])