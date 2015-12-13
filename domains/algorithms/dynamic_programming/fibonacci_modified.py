
#b => t n+1 ,  a => t
def fibonacci(tzero, tone):
  ttwo = tone ** 2 + tzero
  return ttwo, tone

if __name__ == '__main__':
  abn = raw_input().split(' ')
  a, b, n = int(abn[0]), int(abn[1]), int(abn[2])
  for i in range(n-2):
    b, a = fibonacci(a, b)
  print b
