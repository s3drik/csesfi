import sys
a = int(input())

if a in [2, 3]:
    print("NO SOLUTION")
    exit()
if a == 1:
    print(1)
    exit()

sys.stdout.write(" ".join(map(str, range(2, a + 1, 2))) + " ")
sys.stdout.write(" ".join(map(str, range(1, a + 1, 2))))