from collections import Counter

st = input()
maxy = 0
current = 0

for i in range(1, len(st)):
    if st[i] == st[i - 1]:
        current += 1
    else:
        if maxy < current:
            maxy = current  
        current = 0

if(maxy < current):
    maxy = current

print(maxy + 1)