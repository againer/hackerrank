
_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def has_substring(w1, w2, has_common='NO'):
  for letter in _ALPHABET:
    if w1.get(letter, False) and w2.get(letter, False):
      has_common = 'YES'
  return has_common

if __name__ == '__main__':
  t = int(raw_input())
  print '\n'.join([has_substring({letter: True for letter in raw_input()},
                                 {letter: True for letter in raw_input()})
                   for _ in range(t)])
