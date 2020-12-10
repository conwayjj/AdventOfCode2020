def calculatePaths(array):
   #Hack here because there are no two jumps in input
   size = len(array)
   if size == 1 or size == 2:
      return 1
   if size == 3:
      return 2
   if size == 4:
      return 4
   if size == 5:
      return 7
   print("LEN NOT SUPPORTED: ", size)
   return 0
   

with open("input.txt") as file:
   source = file.readlines()

adapters = [0]
for line in source:
   adapters.append(int(line))
   #print(int(line))
adapters.sort()
adapters.append(adapters[-1]+3)
#print (adapters, len(adapters))

differences = {0:0, 1:0, 2:0, 3:0}
threeJumps = [0]
for i in range(1,len(adapters)):
   jump = adapters[i]-adapters[i-1]
   differences[jump] += 1
   if jump == 3:
      threeJumps.append(i)

solution = 1
for i in range(1,len(threeJumps)):
   solution *= calculatePaths(adapters[threeJumps[i-1]:threeJumps[i]])

adapterPaths = {0:1}
for i in range(1,len(adapters)):
   adapter = adapters[i]
  # print (adapter, type(adapter))
   paths = 0
   for j in range(1,4):
      #print (adapter-j)
      if adapter-j in adapterPaths:
         newPaths = adapterPaths[adapter-j]
         paths += adapterPaths[adapter-j]
         #print("PATH: ", adapter, adapter-j, paths, newPaths)
   adapterPaths[adapter] = paths
#print (adapterPaths)
      
print (differences)
print ("1: ", differences[1], "3: ", differences[3])
print ("ANSWER: ", differences[1] * differences[3])
print ("WAYS TO ARRANGE: ", solution)
print("WAYS TO ARRANGE (NO_HACK): ", adapterPaths[adapters[-1]])



