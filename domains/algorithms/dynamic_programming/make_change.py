
def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
   for cents in range(change + 1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change], coinsUsed

def printCoins(coinsUsed, amount_to_change):
   amount = amount_to_change
   while amount > 0:
      thisCoin = coinsUsed[amount]
      print(thisCoin)
      amount = amount - thisCoin

if __name__ == '__main__':
    minCoins, coinsUsed = dpMakeChange([1, 5, 10, 21, 25], 200, [0] * (200 + 1), [0] * (200 + 1))
    printCoins(coinsUsed, 200)
