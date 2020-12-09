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
      target = code[i]



for i in range(len(code)):
   val = 0
   j = i
   while val < target and j < len(code):
      val += code[j]
      if val == target:
         print("Match found from ", i, " to ", j)
         print("MAX: ", max(code[i:j+1]), "MIN: ", min(code[i:j+1]), "SUM: ", max(code[i:j+1]) + min(code[i:j+1]))
         break
      j += 1
