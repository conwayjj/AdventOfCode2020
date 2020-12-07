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
   first = 0
   for person in group:
      personSet = set()
      for answer in person:
         personSet.add(answer)
      if first == 0:
         groupSet = personSet
         first = 1
      else:
         groupSet = groupSet.intersection(personSet)

   #print(groupSet)
   groupSum += len(groupSet)

print (groupSum)
