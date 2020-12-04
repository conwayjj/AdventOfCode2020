with open("""C:\\tmp\\adventCode\\2020\\day1\\input.txt""") as inFile:
    entries = inFile.readlines()

ints = []
for entry in entries:
    ints.append(int(entry))

print (ints)

for numA in ints:
    for numB in ints:
        for numC in ints:
            if numA + numB + numC == 2020:
                print (numA, numB, numC, numA*numB*numC)
