from itertools import combinations

preamble = 25

with open("input.txt") as file:
   source = file.readlines()

code = []
for line in source:
   code.append(int(line))
print (code, len(code))

for i in range(preamble,len(code)):
   #print( i)
   valid = [x + y for x, y in combinations(code[i-preamble:i],2)]
   if code[i] not in valid:
      print (i, code[i])



