n=int(input())
a=0
b=1
while(n):
    if(a<n):
        x=a
    if(a>n):
        y=a
        break 
    c=a+b
    a=b
    b=c
if (n-x<y-n):
    print(x)
elif (n-x==y-n):
    print(x,y)
else:
    print(y)