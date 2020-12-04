with open("""C:\\tmp\\adventCode\\2020\\Nova\\day2\\input.txt""") as inFile:
    lines = inFile.readlines()

validPasswords = 0
invalidPasswords = 0
for line in lines:
    #Example: "5-11 t: glhbttzvzttkdx"
    #print(line)
    words = line.split()
    words[0] = words[0].replace('-',' ')
    howMany = words[0].split()
    howMany[0] = int(howMany[0])
    howMany[1] = int(howMany[1])
    words[1] = words[1].replace(':','')
##    count = words[2].count(words[1])
##    #print (words, howMany, count)
##    if count >= howMany[0] and count <= howMany[1]:
##        validPasswords += 1
##    else:
##        invalidPasswords += 1
    if (words[2][howMany[0]-1] == words[1]) ^ (words[2][howMany[1]-1] == words[1]):
        validPasswords += 1
    else:
        invalidPasswords += 1
    

print("VALID: ", validPasswords)
print("INVALID: ", invalidPasswords)
