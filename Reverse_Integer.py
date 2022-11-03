n=int(input())
x=n
if(x<1):
    n=-x
s=0
while(n):
    r=n%10
    s=s*10+r
    n=n//10
if(x<=1):
    print(-s)
else:
    print(s)
    