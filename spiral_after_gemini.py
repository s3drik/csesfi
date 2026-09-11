import sys


def main():
  # Barcha ma'lumotlarni bir vaqtning o'zida o'qib olamiz (eng tezkor usul)
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  t = int(input_data[0])
  results = []

  idx = 1
  for _ in range(t):
    y = int(input_data[idx])
    x = int(input_data[idx + 1])
    idx += 2

    # Qaysi biri kattaligiga qarab qatlamni (layer) aniqlaymiz
    if y > x:
      if y % 2 == 0:
        ans = y * y - x + 1
      else:
        ans = (y - 1) * (y - 1) + x
    else:
      if x % 2 != 0:
        ans = x * x - y + 1
      else:
        ans = (x - 1) * (x - 1) + y

    results.append(str(ans))

  # Natijalarni bittada ekranga chiqaramiz
  sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
  main()