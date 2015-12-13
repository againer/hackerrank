def deletions_required(input):
  count = 0
  for index, character in enumerate(input):
    if index is not 0:
      if character == input[index - 1]:
        count += 1
  return str(count)


if __name__ == '__main__':
  number_cases = int(raw_input())
  output = [deletions_required(raw_input()) for _ in range(number_cases)]
  print '\n'.join(output)