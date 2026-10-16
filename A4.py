# A4.py | Logic Gates   [5 marks]

a = int(input("Enter A: "))
b = int(input("Enter B: "))

if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("Bits must be 0 or 1")
else:
    print("AND =", a & b)
    print("OR =", a | b)
    print("XOR =", a ^ b)