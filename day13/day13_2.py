import time
import math
from copy import deepcopy

def lcm(x,y):
   return abs(x*y)//math.gcd(x,y)

def timeTilNextBus(t, bus):
   timeSincePrevious = t % bus
   timeRemaining = bus - timeSincePrevious
   if timeRemaining == bus:
      timeRemaining = 0
   return timeRemaining

start = time.perf_counter()
with open("input.txt") as file:
   source = file.readlines()

#print (timeTilNextBus(1,4), timeTilNextBus(2,4), timeTilNextBus(3,4),timeTilNextBus(4,4))
dTime = int(source[0])
#print (dTime)
busses = dict()
count = 0
busA = 0
busB = None
rep = 1
start = 1

for bus in source[1].split(','):
   if bus != 'x':
      busB = int(bus)
      newRep = lcm(rep, busB)
      #print(rep)
      for i in range(start, start+newRep+1, rep):
         #print(i)
         if timeTilNextBus(i, busB) == count%busB:
            print(busB, i, count, newRep)
            rep = newRep
            start = i
            break
         
   count += 1


stop = time.perf_counter()


