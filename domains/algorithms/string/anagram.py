
def anagram_switch_count(word, total_count=0):
  if len(word) % 2 is not 0:
    return -1

  count = [0] * 26

  s1 = word[0:len(word)/2]
  s2 = word[len(word)/2:]

  for letter in s1:
    count[ord(letter) - ord('a')] += 1

  for letter in s2:
    count[ord(letter) - ord('a')] -= 1

  print count

  for x in count:
    total_count += abs(x)

  return total_count/2



if __name__ == '__main__':
  number_of_cases = int(raw_input())
  print '\n'.join([str(anagram_switch_count(raw_input())) for _ in range(number_of_cases)])


  SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID=Customers.CustomerID;