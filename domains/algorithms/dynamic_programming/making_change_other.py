def change(n, coins_available, coins_so_far):
  if sum(coins_so_far) == n:
    yield coins_so_far
  elif sum(coins_so_far) > n:
    pass
  elif coins_available == []:
    pass
  else:
    for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
      yield c
    for c in change(n, coins_available[1:], coins_so_far):
      yield c

if __name__ == '__main__':
  n = 33
  coins = [1, 5, 10, 25]

  solutions = [s for s in change(n, coins, [])]
  for s in solutions:
    print s

  print 'optimal solution:', min(solutions, key=len)

O(number_of_denomications*amount_to_change) runtime, O(n) space.






def dpMakeChange(coinValueList, change , minCoins, coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)