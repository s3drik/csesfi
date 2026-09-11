import sys


def main():
  n = int(sys.stdin.read().strip())

  results = []
  for k in range(1, n + 1):
    total_ways = (k * k * (k * k - 1)) // 2
    attacking_ways = 4 * (k - 1) * (k - 2)
    ans = total_ways - attacking_ways
    results.append(str(ans))

  sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
  main()