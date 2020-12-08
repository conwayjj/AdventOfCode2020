from Processor import Processor
class SolutionFound( Exception ):
    pass
   
with open("input.txt") as file:
   source = file.readlines()

try:
   for i in range(len(source)):
      if source[i][0:3] == "nop" or source[i][0:3] == "jmp":
         #print(i)
         source2 = source.copy()
         if source2[i][0:3] == "nop":
            source2[i] = source2[i].replace("nop", "jmp")
         elif source2[i][0:3] == "jmp":
            source2[i] = source2[i].replace("jmp", "nop")
         proc = Processor(source2)
         PC = 0
         PCs = set()
         while PC not in PCs:
            PCs.add(PC)
            PC = proc.step(debug=False)
            if PC >= len(source2):
               print ("Halting solution found in line ", i, "ACC: ", proc.ACC)
               raise SolutionFound
except SolutionFound:
   pass

