def nop(proc, imm):
    return proc.PC + 1

def acc(proc, imm):
    proc.ACC += int(imm)
    return proc.PC + 1

def jmp(proc, imm):
    return proc.PC + int(imm)


OpCodes =   {'nop': nop,
             'acc': acc,
             'jmp': jmp}
