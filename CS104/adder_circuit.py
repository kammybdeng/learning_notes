def XOR_gate(a, b):
    if a:
        if b:
            return 0
    if a:
        return 1
    if b:
        return 1
    return 0

def AND_gate(a, b):
    if a:
        if b:
            return 1
    return 0

def OR_gate(a, b):
    if a:
        return 1
    if b:
        return 1
    return 0

def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return (s, c)

def full_adder(a, b, c):
    c1 = AND_gate(a, b)
    s1 = half_adder(a, b)[0]
    c2 = AND_gate(s1, c)
    s = half_adder(s1, c)[0]
    c_out = OR_gate(c1, c2)

    return (s, c_out)

def ALU(a, b, c, opcode):
    if opcode == 0:
        s, c = half_adder(a,b)
    else:
        s, c = full_adder(a, b, c)
    return (s, c)

## TEST
a = 0
b = 0
c = 1
opcode = 0
print(half_adder(a, b))
print(full_adder(a, b, c))
print(ALU(a, b, c, opcode))
