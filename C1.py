# C1.py | Current and Power [5 marks]

def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return i * i * r

current = ohms_current(12, 6)
power = power_dissipated(current, 6)
print("Current =", current, "A")
print("Power =", power, "W")

current = ohms_current(9, 3)
power = power_dissipated(current, 3)
print("Current =", current, "A")
print("Power =", power, "W")