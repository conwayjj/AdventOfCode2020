import time
import math
from copy import deepcopy

debug = False

def dp(*args):
   if debug:
      print(args)

start = time.perf_counter()
ANDMASK = 2**36-1
ORMASK = 0

def mask(x, ANDMASK, ORMASK):
   dp("Used masks: AND ", 2**36 - ANDMASK - 1, " OR ", ORMASK, "on",x,((x & ANDMASK) | ORMASK) )
   return ((x & ANDMASK) | ORMASK)

def updateMask(newMask):
   ANDMASK = 2**36-1
   ORMASK = 0
   for i in range(36):
      if newMask[i] == '0':
         ANDMASK -= 2** (35 - i)
      elif newMask[i] == '1':
         ORMASK += 2 ** (35 - i)
   dp("Updated masks: AND ", 2**36 - ANDMASK - 1, " OR ", ORMASK, newMask)
   return ANDMASK, ORMASK
      
with open("input.txt") as file:
   source = file.readlines()


mem = dict()
for line in source:
   words = line.split()
   if words[0] == "mask":
      ANDMASK, ORMASK = updateMask(words[2])
   elif words[0][0:3] == "mem":
      address = int(words[0][4:-1])
      masked = mask(int(words[2]), ANDMASK, ORMASK)
      mem[address] = masked
      dp("Wrote: ", int(words[2]), masked, " to ", address)

total = 0
for loc in mem:
   dp(loc, mem[loc])
   total += mem[loc]
      
print("TOTAL: ", total)

stop = time.perf_counter()
print("TIME: ", stop-start)

