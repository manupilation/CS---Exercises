def count_number(n):
    if n == 0:
      return 0
    print(n)
    return n + count_number(n - 1)

print(count_number(14))
