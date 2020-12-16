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
      
with open("input.txt") as file:
   source = file.readlines()

numbers = dict()
count = 1
prev = 0
for number in source[0].split(','):
   number = int(number)
   numbers[number] = count
   dp(number, count)
   count += 1
   prev = number
   nex = 0

while count <= 2020:
   number = nex
   if number in numbers:
      nex = count - numbers[number]
   else:
      nex = 0
   numbers[number] = count
   dp(number, count)
   count += 1
      

print("2020:", number, count)
stop = time.perf_counter()
print("TIME: ", stop-start)

