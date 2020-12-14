import time
import numpy as np
from copy import deepcopy

start = time.perf_counter()
with open("input.txt") as file:
   source = file.readlines()

heading = [1,0]
newHeading = [0,0]
location = [0,0]
for line in source:
   command = line[0]
   value = int(line[1:])
   print(command,value)
   if command == 'N':
      location[1] += value
   elif command == 'S':
      location[1] -= value
   elif command == 'E':
      location[0] += value
   elif command == 'W':
      location[0] -= value
   elif command == 'F':
      location[0] += heading[0] * value
      location[1] += heading[1] * value
   elif command == 'R':
      while value >= 90:
         value -= 90
         newHeading[0] = heading[1]
         newHeading[1] = -heading[0]
         heading[0] = newHeading[0]
         heading[1] = newHeading[1]
      if value > 0:
         print("Remainder: ", value)

   elif command == 'L':
      while value >= 90:
         value -= 90
         newHeading[0] = -heading[1]
         newHeading[1] = heading[0]
         heading[0] = newHeading[0]
         heading[1] = newHeading[1]
      if value > 0:
         print("Remainder: ", value)

   print (heading, location)

print("LOCATION: ", location, " MANHATTAN: ", abs(location[0]) + abs(location[1]))
stop = time.perf_counter()


