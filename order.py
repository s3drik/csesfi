import sys

n = int(sys.stdin.readline())
data = map(int, sys.stdin.readline().split())

prev = 0
count = 0

for i in data:
    if (moj := prev - i) > 0:
        # print(moj)
        count += moj
    else:
        prev = i
    # print(prev, i)

print(count)
# print([d for d in data])