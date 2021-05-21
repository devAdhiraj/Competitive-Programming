a = int(input())
for i in range (a):
  s = input()
  c = 1
  i = 1
  while(i <= len(s)):
    c = 1  
    while(i <= len(s) - 1 and s[i] == s[i - 1] ):
      c += 1
      i += 1
    i += 1
    print(str(c), s[i - 2] + " ", end='')
  print()
