import time
from copy import deepcopy

start = time.perf_counter()
with open("input.txt") as file:
   source = file.readlines()

dTime = int(source[0])
print (dTime)
busses = dict()
for bus in source[1].split(','):
   if bus != 'x':
      bus = int(bus)
      busses[bus] = bus - (dTime % bus)

print (busses, min(busses))
minWait = 9999999
minBus = None
for bus in busses:
   if busses[bus] < minWait:
      minWait = busses[bus]
      minBus = bus

print(minBus, minWait, minWait*minBus)
   
stop = time.perf_counter()


