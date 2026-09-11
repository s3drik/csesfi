n = int(input())
print(n)
while n!=1:
    if n%2:
        print(n:= n*3 + 1, end=' ')
    else:
        print(n:= n//2, end=' ')
