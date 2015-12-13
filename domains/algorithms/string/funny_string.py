def is_funny(s, r):
  return [abs(ord(s[index]) - ord(s[index - 1])) == abs(ord(r[index]) - ord(r[index - 1]))
          for index in range(1, len(s))]


if __name__ == '__main__':
  number_of_inputs = int(raw_input())
  output = []
  for i in range(number_of_inputs):
    s = str(raw_input())
    output.append('Not Funny' if False in is_funny(s, s[::-1]) else 'Funny')
  print '\n'.join(output)
