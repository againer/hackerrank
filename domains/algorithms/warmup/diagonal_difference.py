
def get_diagonal_sums_difference(square):
  return abs(sum([square[index][index] for index in range(0, len(square))]) -
             sum([square[(len(square) - 1) - index][index] for index in range(0, len(square))]))

if __name__ == '__main__':
  print get_diagonal_sums_difference([[int(digit) for digit in raw_input().split()] for _ in range(int(raw_input()))])
