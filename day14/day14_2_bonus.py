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
MASKSTRING = "000000000000000000000000000000000000"

def mask(x, ANDMASK, ORMASK):
   #dp("Used masks: AND ", 2**36 - ANDMASK - 1, " OR ", ORMASK, "on",x,((x & ANDMASK) | ORMASK) )
   return ((x & ANDMASK) | ORMASK)

def enumerateMasks(x, mask):
   numFloats = mask.count('X')
   address = ""
   for i in range(36):
      if mask[i] == '0':
         address += str((x & (2 ** (35-i))) >> (35 - i))
      else:
         address += mask[i]
   masks = []
   print("Enumerating", 2**numFloats,"masks")
   for i in range(2**numFloats):
      k = 0
      newMask = 0
      for j in range(36):
         if mask[j] == '0':
            newMask += x & (2 ** (35-j))
         elif mask[j] == '1':
            newMask += 2**(35-j)
         elif mask[j] == 'X':
            newMask += 2**(35-j) if (i & (2**(numFloats-k-1)))>>(numFloats-k-1) == 1 else 0
            k += 1
      masks.append(newMask)
   #dp (mask, x, address)
   #dp (masks)
   return masks

def updateMask(newMask):
   ANDMASK = 2**36-1
   ORMASK = 0
   for i in range(36):
      if newMask[i] == '0':
         ANDMASK -= 2** (35 - i)
      elif newMask[i] == '1':
         ORMASK += 2 ** (35 - i)
   #dp("Updated masks: AND ", 2**36 - ANDMASK - 1, " OR ", ORMASK, newMask)
   return ANDMASK, ORMASK, newMask
      
with open("bonus.txt") as file:
   source = file.readlines()


mem = dict()
for line in source:
   words = line.split()
   if words[0] == "mask":
      ANDMASK, ORMASK, MASKSTRING = updateMask(words[2])
   elif words[0][0:3] == "mem":
      address = int(words[0][4:-1])
      #masked = mask(int(words[2]), ANDMASK, ORMASK)
      enumerateMasks(address, MASKSTRING)
      for address in enumerateMasks(address, MASKSTRING):
         mem[address] = int(words[2])
      #dp("Wrote: ", int(words[2]), int(words[2]), " to ", address)

total = 0
for loc in mem:
   #dp(loc, mem[loc])
   total += mem[loc]
      
print("TOTAL: ", total)

stop = time.perf_counter()
print("TIME: ", stop-start)

