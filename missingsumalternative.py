n = int(input())

nums = map(int, input().split())

s = n

for num, i in enumerate(nums, start=1):
    s ^= i ^ num

print(s)