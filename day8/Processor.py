import threading
from Ops import OpCodes

class Processor:
    PC = 0
    RB = 0
    ACC = 0

    def getInput(self):
        return int(input("INPUT:"))

    def sendOutput(self, outVal):
        print("OUTPUT:",outVal)
        return
    
    def processNextInstruction(self, debug = False):
        instruction = self.source[self.PC]
        opCode, imm = instruction.split()
        if debug:
            print(opCode, imm, self.PC, self.ACC)
        if opCode in OpCodes:
            return OpCodes[opCode](self, imm)
        else:
            print("Unexpected command %s at location: %d" % (instruction,self.PC))
            return -1

    def run(self):
        self.PC = 0
        self.RB = 0
        while self.PC >= 0:
            self.PC = self.processNextInstruction()

    def step(self, debug = False):
        self.PC = self.processNextInstruction(debug)
        return self.PC

    def forkAndRun(self):
        p = threading.Thread(target=self.run)
        p.start()
        return p
    
    def __init__(self, source, getInput=None, sendOutput=None):
        self.source = source.copy()
        self.PC = 0
        self.RB = 0
        self.ACC = 0
        if getInput != None:
            self.getInput = getInput
        if sendOutput != None:
            self.sendOutput = sendOutput
