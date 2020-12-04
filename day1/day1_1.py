with open("""C:\\tmp\\adventCode\\2020\\day1\\input.txt""") as inFile:
    entries = inFile.readlines()

ints = []
for entry in entries:
    ints.append(int(entry))

print (ints)

for numA in ints:
    for numB in ints:
        if numA + numB == 2020:
            print (numA, numB, numA*numB)
