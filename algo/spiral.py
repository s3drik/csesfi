import sys

n = int(sys.stdin.readline())

tests = sys.stdin.readlines()

def finder(x : int, y : int) -> int:
    greater = max(x, y)

    if greater == x:
        ind = 0
    else:
        ind = 1
    
    if greater & 1:
        if ind:
            return y*y - x + 1
        else:
            return (x-1)**2 + y
    else:
        if ind:
            return (y-1)**2 + x
        else:
            return x*x - y + 1


for i in tests:
    a, b = map(int, i.split())
    print(finder(a, b))
