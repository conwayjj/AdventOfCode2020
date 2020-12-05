def translateBinary(string, zero='0', one='1'):
   outVal = 0
   size = len(string)
   for i in range(size):
      if string[i] == one:
         outVal += 2 ** (size-i-1)
      elif string[i] != zero:
         print("Unexpected character: ", string[i])
   return outVal
      
with open(""".\\input.txt""") as inFile:
    lines = inFile.readlines()

seats = []
for line in lines:
   seatID = translateBinary(line[0:7], 'F','B')*8 + translateBinary(line[7:10],'L','R')
   #print(line, seatID)
   seats.append(seatID)

#print(seats)
seats.sort()
print(seats)
for i in range(1,len(seats)):
   if seats[i-1]+1 != seats[i]:
      print("Hole found, missing seatID between:", seats[i-1], " and ", seats[i])
print ("Highest seat ID:", seats[-1])
