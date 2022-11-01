a=int(input())
b=int(input())
def ispalin(n):
    if(n==int(str(n)[::-1])):
        return 1
    else:
        return 0
for i in range(a,b+1):
    if(ispalin(i)==1):
        print(i,end=' ')