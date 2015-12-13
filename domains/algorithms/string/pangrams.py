
_ALPHABEES = 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(sentence):
  return not(False in [letter in sentence.lower() for letter in _ALPHABEES])

if __name__ == '__main__':
  sentence = str(raw_input())
  print 'pangram' if is_pangram(sentence) else 'not pangram'