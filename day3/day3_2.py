def calcCollisions(lines, right, down):
   X = 0
   O = 0
   row = 0
   slope = right/down

   for line in lines:
      #print (line)
      if row % down == 0:
         line = line.replace('\n','')
         if line[int(row*slope) % len(line)] == '#':
            char = 'X'
            X += 1
         else:
            char = 'O'
            O += 1
##         string = ['.']
##         for i in range(0,int(row*slope)):
##            string.append(line[i%len(line)])
##         string[int(row*slope)] = char
##         print (string)
            
      row += 1

   print ("Slope: ", down,"/",right, " X: ",X," O: ",O)
   return X
   


with open("""C:\\tmp\\adventCode\\2020\\day3\\input.txt""") as inFile:
    lines = inFile.readlines()

collisions = 1
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
   collisions *= calcCollisions(lines, slope[0], slope[1])

print(collisions)


