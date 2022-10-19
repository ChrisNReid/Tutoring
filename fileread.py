with open('words.txt') as f:
  for line in f:
#strip, is opposite of split. removes array
    print(line.strip())
    if 'str' in line:
      break