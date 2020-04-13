def NAND(a, b):
    if a == 1 and b == 1:
        return False
    return True


def NOR(a, b):
    if (a == 0) and (b == 0):
        return 1
    elif (a == 0) and (b == 1):
        return 0
    elif (a == 1) and (b == 0):
        return 0
    return 0


def NOT(a):
    if a == 0:
        return 1
    return 0


def OR(a, b):
    if a == 1:
        return True
    elif b == 1:
        return True
    return False


def XOR (a, b):
    if a != b:
        return 1
    return 0


def AND(a, b):
    if a == 1 and b == 1:
        return True
    return False


i = input()
if i == 'NAND':
    print(" NAND Truth Table ")
    print(" A = False, B = False | A NAND B =", NAND(False, False), " | ")
    print(" A = False, B = True | A NAND B =", NAND(False, True), " | ")
    print(" A = True, B = False | A NAND B =", NAND(True, False), " | ")
    print(" A = True, B = True | A NAND B =", NAND(True, True), " | ")

elif i == 'NOR':
    print("NOR Truth Table ")
    print(" A = False, B = False | A NOR B =", NOR(False, False), " | ")
    print(" A = False, B = True | A NOR B =", NOR(False, True), " | ")
    print(" A = True, B = False | A NOR B =", NOR(True, False), " | ")
    print(" A = True, B = True | A NOR B =", NOR(True, True), " | ")
elif i == 'NOT':
    print("  NOT Truth Table ")
    print(" A = False | A NOT =", NOT(False), " | ")
    print(" A = True, | A NOT =", NOT(True), " | ")
elif i == 'OR':
    print(" OR Truth Table ")
    print(" A = False, B = False | A OR B =", OR(False, False), " | ")
    print(" A = False, B = True | A OR B =", OR(False, True), " | ")
    print(" A = True, B = False | A OR B =", OR(True, False), " | ")
    print(" A = True, B = True | A OR B =", OR(True, True), " | ")
elif i == 'XOR':
    print(" XOR Truth Table")
    print(" A = False, B = False | A XOR B =", XOR(False, False), " | ")
    print(" A = False, B = True | A XOR B =", XOR(False, True), " | ")
    print(" A = True, B = False | A XOR B =", XOR(True, False), " | ")
    print(" A = True, B = True | A XOR B =", XOR(True, True), " | ")
elif i == 'AND':
    print(" AND Truth Table")
    print(" A = False, B = False | A AND B =", AND(False, False), " | ")
    print(" A = False, B = True | A AND B =", AND(False, True), " | ")
    print(" A = True, B = False | A AND B =", AND(True, False), " | ")
    print(" A = True, B = True | A AND B =", AND(True, True), " | ")

