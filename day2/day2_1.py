

def validatePassword(password):
  words = password.split()
  lower, upper = words[0].split('-')
  lower = int(lower)
  upper = int(upper)
  character = words[1][0]
  pw = words[2]
  count = pw.count(character)
  if count >= lower and count <= upper:
      return True
  else:
      return False
    
with open("""C:\\tmp\\adventCode\\2020\\day2\\input.txt""") as inFile:
    lines = inFile.readlines()

validPasswords = 0
invalidPasswords = 0
for line in lines:
    if validatePassword(line):
        validPasswords += 1
    else:
        invalidPasswords += 1

print("VALID: ", validPasswords)
print("INVALID: ", invalidPasswords)
