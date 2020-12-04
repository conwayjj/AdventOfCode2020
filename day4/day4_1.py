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
        setattr(self,attr,val)
      #print (self)

   def __repr__(self):
      return("PASSPORT <pid = {}, cid = {}, ecl = {}, hcl = {}\n" + \
                  "          hgt = {}, eyr = {}, iyr = {}, byr = {}").format( \
                  self.pid, self.cid, self.ecl, self.hcl, \
                  self.hgt, self.eyr, self.iyr, self.byr)

   def isValid(self):
      return( self.byr != None and \
         self.iyr != None and \
         self.eyr != None and \
         self.hgt != None and \
         self.hcl != None and \
         self.ecl != None and \
         self.pid != None)
         
   


with open("""C:\\tmp\\adventCode\\2020\\day4\\input.txt""") as inFile:
    lines = inFile.readlines()

passports = []
currentString = ""
for line in lines:
   if len(line) > 1:
      currentString += line
   else:
      #print(currentString)
      passports.append(passport(currentString))
      currentString = ""
if currentString != "":
   #print(currentString)
   passports.append(passport(currentString))
   currentString = ""

count = 0
for pp in passports:
   if pp.isValid():
      count += 1
print ("Valid Passports: ", count)
