class passport:
   byr = None
   iyr = None
   eyr = None
   hgt = None
   hcl = None
   ecl = None
   pid = None
   cid = None

   def __init__(self, initString):
      for field in initString.split():
        attr,val = field.split(':')
        if attr == 'byr':
           self.setBYR(val)
        elif attr == 'iyr':
           self.setIYR(val)
        elif attr == 'eyr':
           self.setEYR(val)
        elif attr == 'hgt':
           self.setHGT(val)
        elif attr == 'hcl':
           self.setHCL(val)
        elif attr == 'ecl':
           self.setECL(val)
        elif attr == 'pid':
           self.setPID(val)
        elif attr == 'cid':
           self.setCID(val)
        
      print (self)

   def __repr__(self):
      return("PASSPORT <IsVALID? = {}, pid = {}, cid = {}, ecl = {}, hcl = {}\n" + \
                  "          hgt = {}, eyr = {}, iyr = {}, byr = {}>").format( \
                  self.isValid(), self.pid, self.cid, self.ecl, self.hcl, \
                  self.hgt, self.eyr, self.iyr, self.byr)

   def setBYR(self, val):
      self.byr = int(val)

   def setIYR(self, val):
      self.iyr = int(val)

   def setEYR(self, val):
      self.eyr = int(val)

   def setHGT(self, val):
      self.hgt = val

   def setHCL(self, val):
      self.hcl = val

   def setECL(self, val):
      self.ecl= val

   def setPID(self, val):
      self.pid = val

   def setCID(self, val):
      self.cid = val

   def isBYRValid(self):
      return self.byr != None and self.byr >= 1920 and self.byr <= 2002

   def isIYRValid(self):
      return self.iyr != None and self.iyr >= 2010 and self.iyr <= 2020

   def isEYRValid(self):
      return self.eyr != None and self.eyr >= 2020 and self.eyr <= 2030

   def isHGTValid(self):
      valid = False
      if self.hgt != None:
         if self.hgt[-2:] == 'cm':
            if int(self.hgt[:-2]) >= 150 and int(self.hgt[:-2]) <= 193:
               valid = True
         elif self.hgt[-2:] == 'in':
            if int(self.hgt[:-2]) >= 59 and int(self.hgt[:-2]) <= 76:
               valid = True
      return valid

   def isHCLValid(self):
      validChars = "0123456789abcdef"
      #print (self.hcl)
      valid = self.hcl != None and \
             len(self.hcl) == 7 and \
             self.hcl[0] == '#' and \
             all(self.hcl[x] in validChars for x in range(1,7))
      #print(valid)
      return valid

   def isECLValid(self):
      validColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
      return (self.ecl != None and \
              self.ecl in validColors)

   def isPIDValid(self):
      validChars = "0123456789"
      return (self.pid != None and \
              len(self.pid) == 9 and \
              all(self.pid[x] in validChars for x in range(0,9)))

   def isCIDValid(self):
      return True
   
   def isValid(self):
      return(self.isBYRValid() and \
             self.isIYRValid() and \
             self.isEYRValid() and \
             self.isHGTValid() and \
             self.isHCLValid() and \
             self.isECLValid() and \
             self.isPIDValid() and \
             self.isCIDValid())
         
              
         
   



with open("""C:\\tmp\\adventCode\\2020\\day4\\input.txt""") as inFile:
    lines = inFile.readlines()

passports = []
currentString = ""
for line in lines:
   if len(line) > 1:
      currentString += line
   else:
      print(currentString.replace('\n',' '))
      passports.append(passport(currentString.replace('\n',' ')))
      currentString = ""
if currentString != "":
   print(currentString)
   passports.append(passport(currentString.replace('\n',' ')))
   currentString = ""

count = 0
for pp in passports:
   if pp.isValid():
      count += 1
print ("Valid Passports: ", count)
