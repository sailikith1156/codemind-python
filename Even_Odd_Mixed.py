n=input()
e=o=0
for i in range(len(n)):
    if(int(n[i])%2==0):
        e+=1
    if(int(n[i])%2==1):
        o+=1
if(len(n)==e):
    print("Even")
elif(len(n)==o):
    print('Odd')
else:
    print('Mixed')