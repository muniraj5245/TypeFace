n = int(input())
if n == 0:
    print(0)
string=''
while n:
    n, r = divmod(n,3)
    string=string+str(r)
print(string)