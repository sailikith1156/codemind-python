n=int(input())
cnt=0
def isprime(n):
    if(n<=1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
for i in range(1,n+1):
    if(n%i==0 and isprime(i)==0):
        cnt+=1
print(cnt)