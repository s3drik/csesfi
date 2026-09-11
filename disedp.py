n = int(input())

dp = [0] * (n+1)

dp[0] = 1


for i in range(1, n+1):
    for j in range(1, 7):
        if i >= j:
            dp[i] = (dp[i] + dp[i - j]) % (1e9 + 7)
        else:
            break

print(int(dp[-1]))