
n = int(input())

nums = map(int, input().split())

som = n * (n+1) // 2


print(som - sum(nums))