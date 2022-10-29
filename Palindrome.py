def reverse(num):
    rev = 0
    while num > 0:
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    return rev
    
n = int(input())
if n == reverse(n):
    print('True')
else:
    print('False')