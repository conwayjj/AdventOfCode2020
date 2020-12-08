from Processor import Processor

with open("input.txt") as file:
   source = file.readlines()

proc = Processor(source)

PC = 0
PCs = set()
while PC not in PCs:
   PCs.add(PC)
   PC = proc.step(debug=True)
