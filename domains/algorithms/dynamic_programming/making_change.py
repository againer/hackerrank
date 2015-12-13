

def make_change(n, coins_available, coins_so_far):
  if sum(coins_so_far) == n:
    yield coins_so_far
  elif sum(coins_so_far) > n:
    pass
  elif coins_available == []:
    pass
  else:
    for c in make_change(n, coins_available[:], coins_so_far+[coins_available[0]]):
      yield c
    for c in make_change(n, coins_available[1:], coins_so_far):
      yield c




if __name__ == '__main__':
  n, m = raw_input().split()
  total_change, m = int(n), int(m)
  denominations = [int(amount) for amount in raw_input().split()]
  print n, denominations

  print [_ for _ in make_change(n, denominations, [])]
