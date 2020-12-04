with open("""C:\\tmp\\adventCode\\2020\\Nova\\day1\\input.txt""") as inFile:
    lines = inFile.readlines()

numbers = []
for line in lines:
    numbers.append(int(line))

#print (numbers, len(numbers))

for numberA in numbers:
  for numberB in numbers:
      if numberA + numberB == 2020:
        print(numberA, " + ", numberB, " = ", numberA + numberB)
        print(numberA, " * ", numberB, " = ", numberA * numberB)
      
#print (numbers, len(numbers))
