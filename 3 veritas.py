def NAND (a, b):
    if a == 1 and b == 1:
        return False
    else:
        return True

def NOR(a, b):
    if (a == 0) and (b == 0):
        return 1
    elif (a == 0) and (b == 1):
        return 0
    elif (a == 1) and (b == 0):
        return 0
    elif (a == 1) and (b == 1):
        return 0

def NOT(a):
    if(a == 0):
        return 1
    elif(a == 1):
        return 0
def OR(a, b):
    if a == 1:
        return True
    elif b == 1:
        return True
    else:
        return False
def XOR (a, b):
    if a != b:
        return 1
    else:
        return 0
def AND(a, b):
    if a == 1 and b == 1:
        return True
    else:
        return False
i=input()
if i=='NAND':
    print(" NAND Truth Table ")
    print(" A = False, B = False | A AND B =", NAND(False, False), " | ")
    print(" A = False, B = True | A AND B =", NAND(False, True), " | ")
    print(" A = True, B = False | A AND B =", NAND(True, False), " | ")
    print(" A = True, B = True | A AND B =", NAND(True, True), " | ")

elif i=='NOR':
    print("NOR Truth Table ")
    print(" A = False, B = False | A AND B =", NOR(False, False), " | ")
    print(" A = False, B = True | A AND B =", NOR(False, True), " | ")
    print(" A = True, B = False | A AND B =", NOR(True, False), " | ")
    print(" A = True, B = True | A AND B =", NOR(True, True), " | ")
elif i=='NOT':
    print("  NOT Truth Table ")
    print(" A = False | A NOT =", NOT(False), " | ")
    print(" A = True, | A NOT =", NOT(True), " | ")
elif i=='OR':
    print(" OR Truth Table ")
    print(" A = False, B = False | A AND B =", OR(False, False), " | ")
    print(" A = False, B = True | A AND B =", OR(False, True), " | ")
    print(" A = True, B = False | A AND B =", OR(True, False), " | ")
    print(" A = True, B = True | A AND B =", OR(True, True), " | ")
elif i=='XOR':
    print(" XOR Truth Table")
    print(" A = False, B = False | A AND B =", XOR(False, False), " | ")
    print(" A = False, B = True | A AND B =", XOR(False, True), " | ")
    print(" A = True, B = False | A AND B =", XOR(True, False), " | ")
    print(" A = True, B = True | A AND B =", XOR(True, True), " | ")
elif i=='AND':
    print(" AND Truth Table")
    print(" A = False, B = False | A AND B =", AND(False, False), " | ")
    print(" A = False, B = True | A AND B =", AND(False, True), " | ")
    print(" A = True, B = False | A AND B =", AND(True, False), " | ")
    print(" A = True, B = True | A AND B =", AND(True, True), " | ")