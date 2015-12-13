def quickSort(ar):
  if len(ar) == 0:
    return ar
  if len(ar) == 1:
    return [ar[0]]
  else:
    left = quickSort([x for x in ar[1:] if x <= ar[0]])
    right = quickSort([x for x in ar[1:] if x > ar[0]])
    print ' '.join([str(x) for x in (left + [ar[0]] + right)])
    return left + [ar[0]] + right

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)