with open("""C:\\tmp\\adventCode\\2020\\day3\\input.txt""") as inFile:
    lines = inFile.readlines()

X = 0
O = 0
row = 0

for line in lines:
   line = line[:-1]
   print (line)
   if line[row*3 % len(line)] == '#':
      char = 'X'
      X += 1
   else:
      char = 'O'
      O += 1
   string = ['.']
   for i in range(0,row*3):
      string.append(line[i%len(line)])
   string[row*3] = char
   #print (string)
         
   row += 1

print ("X: ",X," O: ",O)
