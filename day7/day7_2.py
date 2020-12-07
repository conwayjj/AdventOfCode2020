bagList = dict()

def getContents(bag):
   returnList = [bag]
   #print("GC:", bag)
   for contentbag in bagList[bag]:
      #print("CB:",contentbag)
      for item in getContents(contentbag):
         #print("CBI:", item)
         returnList.append(item)
   return returnList

with open("input.txt") as file:
   lines = file.readlines()


for line in lines:
   line = line.replace('\n', '')
   line = line.replace('.','')
   line = line.replace('bags', 'bag')
   holder, contents = line.split(" contain ")
   if contents == "no other bag":
      contents = []
   else:
      contents = contents.split(', ')
   contentsArray = []
   for content in contents:
      for i in range(int(content[0])):
         contentsArray.append(content[2:])
   bagList[holder] = contentsArray

#print(bagList)

shinyGoldBag = getContents("shiny gold bag")
      
#print("SHINY:", shinyGoldBag, len(shinyGoldBag)-1)
print("SHINY:", len(shinyGoldBag)-1)
