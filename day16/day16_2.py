import time
import math
from copy import deepcopy

debug = False

class rule:
   min1 = 0
   min2 = 0
   max1 = 0
   max2 = 0
   name = "UNINITIALIZED"
   possible = []

   def __init__(self, name, min1, max1, min2, max2):
      self.name = name
      self.min1 = int(min1)
      self.max1 = int(max1)
      self.min2 = int(min2)
      self.max2 = int(max2)

   def __repr__(self):
      return '<RULE: ' + self.name + ' = ' + \
             str(self.min1) + ' - ' + str(self.max1) + ' or ' + \
             str(self.min2) + ' - ' + str(self.max2) + str(self.possible) + " >" 

   def contains(self, val):
      return (val >= self.min1 and val <= self.max1) or \
             (val >= self.min2 and val <= self.max2)
   
def dp(*args):
   if debug:
      print(args)

start = time.perf_counter()
      
with open("input.txt") as file:
   source = file.readlines()

rules = []
tickets = []
i = 0
line = source[i].strip()
while line != "":
   print(line)
   name, words = line.split(':')
   words = words.split()
   min1, max1 = words[0].split("-")
   min2, max2 = words[2].split("-")
   rules.append(rule(name,min1,max1,min2,max2))
   i+= 1
   line = source[i].strip()

i += 2
myTicket = [int(x) for x in source[i].strip().split(',')]

i+= 3
while i<len(source):
   tickets.append([int(x) for x in source[i].strip().split(',')])
   i+= 1
   
#print (rules)
#print (myTicket)
#print (tickets)

badEntries = []
badTickets = []
for ticket in tickets:
   badTicket = False
   for entry in ticket:
      bad = True
      for rule in rules:
         if rule.contains(entry):
            bad = False
            break
      if bad:
         badEntries.append(entry)
         badTicket = True
   if badTicket:
      badTickets.append(ticket)

for ticket in badTickets:
   tickets.remove(ticket)

#print (badEntries, sum(badEntries))
#print (tickets)

numFields = len(myTicket)
for rule in rules:
   rule.possible = list(range(numFields))

possibleRules = []
for i in range(numFields):
   possibleRules.append(dict())
   for j in range(len(rules)):
      possibleRules[i][j] = rules[j]

print (rules)
for ticket in tickets:
   for i in range(len(ticket)):
      toRemove = []
      for rule in possibleRules[i]:
         if not possibleRules[i][rule].contains(ticket[i]):
            toRemove.append(rule)
      for rule in toRemove:
         del possibleRules[i][rule]

for i in range(len(possibleRules)):
   print (i, [possibleRules[i][rule].name for rule in possibleRules[i]])

for i in range(len(possibleRules)):
   singleRules = []
   for rules in possibleRules:
      if len(rules) == 1:
         for rule in rules:
            singleRules.append(rule)
            #print("SINGLE:", rules[rule])
   for rule in singleRules:
      for rules in possibleRules:
         #print (rules)
         if len(rules) > 1 and rule in rules:
            #print("REMOVING", rules[rule])
            del rules[rule]
print('----------------------------')
for i in range(len(possibleRules)):
   print (i, [possibleRules[i][rule].name for rule in possibleRules[i]])

result = 1   
for i in range(len(possibleRules)):
   for rule in possibleRules[i]:
      if 'departure' in possibleRules[i][rule].name:
         result *= myTicket[i]

print("RESULT:", result)   
stop = time.perf_counter()
print("TIME: ", stop-start)
