n, x = map(int, input().split())

nums = list(map(int, input().split()))

paired = {}

for num, i in enumerate(nums, start=1):
    paired[i] = num


def pr(a, b, c, d):
    print(paired[a], paired[b], paired[c], paired[d])
    exit()

c1, c2 = 0, 1
o1, o2 = n-2, n-1

# c1 c2 ..... o1 o2
nums.sort()

while nums[c2] < nums[o1] and nums[c2-c1] != 1 and nums[o2-o1] != 1:
    s = nums[c1] + nums[c2] + nums[o1] + nums[o2] - x
    if s == 0:
        pr(nums[o1], nums[o2], nums[c1], nums[c2])
    if s < 0:
        if o2-o1 == 1:
            o1 -= 1
            o2 = n-1
        else:
            o2 -= 1
    else:
        if c2 - c1 == 1:
            c2 += 1
            c1 = 0
        else:
            c1 += 1
    print(c1, c2, o1, o2)

print("IMPOSSIBLE")