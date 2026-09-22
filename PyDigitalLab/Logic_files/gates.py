#This is the file containing all functions of gates
def not_g(a):
    if not isinstance(a, int):
        raise ValueError("Invalid input of not_g: input of not gate can only be integer")
    if a not in (0, 1, True, False):
        raise ValueError("Invalid input of not_g: input of not gate should be 0/1/True/False")
    return 1-a

def or_g(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input of or_g: both inputs of 'or gate' can only be integers")
    if a not in (0, 1, True, False) or b not in (0, 1, True, False):
        raise ValueError("Invalid input of or_g: both inputs of 'or gate' should be 0/1/True/False")
    return a | b

def and_g(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input of and_g: both inputs of 'and gate' can only be integers")
    if a not in (0, 1, True, False) or b not in (0, 1, True, False):
        raise ValueError("Invalid input of and_g: both inputs of 'and gate' should be 0/1/True/False")
    return a & b

def nand_g(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input of nand_g: both inputs of 'nand gate' can only be integers")
    if a not in (0, 1, True, False) or b not in (0, 1, True, False):
        raise ValueError("Invalid input of nand_g: both inputs of 'nand gate' should be 0/1/True/False")
    return 1-(a & b)

def nor_g(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input of nor_g: both inputs of 'nor gate' can only be integers")
    if a not in (0, 1, True, False) or b not in (0, 1, True, False):
        raise ValueError("Invalid input of nor_g: both inputs of 'nor gate' should be 0/1/True/False")
    return 1-(a | b)

def xor_g(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input of xor_g: both inputs of 'xor gate' can only be integers")
    if a not in (0, 1, True, False) or b not in (0, 1, True, False):
        raise ValueError("Invalid input of xor_g: both inputs of 'xor gate' should be 0/1/True/False")
    return a ^ b

def xnor_g(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input of xnor_g: both inputs of 'xnor gate' can only be integers")
    if a not in (0, 1, True, False) or b not in (0, 1, True, False):
        raise ValueError("Invalid input of xnor_g: both inputs of 'xnor gate' should be 0/1/True/False")
    return 1-(a ^ b)