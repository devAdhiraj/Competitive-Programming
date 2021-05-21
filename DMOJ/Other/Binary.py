# Using built-in bin() function in python
for i in range(int(input())):
    a = bin(int(input())).split('b')[1]
    a = (4 - len(a) % 4) % 4 * "0" + a
    for i in range(0, len(a) - 1, 4):
        print(a[i : i + 4], end= " ")
    print()
    
# Solution without using bin() - can probably be optimized using log
c = int(input())
for i in range(c):
  a = int(input())
  s = str(a % 2)
  while a // 2:
    a //= 2
    if (s.count("1") + s.count("0")) % 4 ==  0:
      s += " "
    s += str(a % 2)
  while (s.count("1") + s.count("0")) % 4:
    s += "0"
  print(s[::-1])
  
