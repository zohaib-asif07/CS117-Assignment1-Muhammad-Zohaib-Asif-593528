# B1.py | Ohm's Law Table   [5 marks]

resistance = 10

for voltage in range(1, 11):
    current = voltage / resistance
    print("V =", voltage, "V, I =", current, "A")