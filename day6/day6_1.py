with open("input.txt") as file:
   lines = file.readlines()
   
groups = []
groups.append([])
for line in lines:
   line = line.replace('\n','')
   if line == '':
      groups.append([])
   else:
      groups[len(groups)-1].append(line)

#print (groups)

groupSum = 0
for group in groups:
   groupSet = set()
   for person in group:
      for answer in person:
         groupSet.add(answer)

   #print(groupSet)
   groupSum += len(groupSet)

print (groupSum)
