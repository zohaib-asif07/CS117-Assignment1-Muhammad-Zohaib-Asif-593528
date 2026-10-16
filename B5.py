# B5.py | Resistor Tolerance Sorting   [10 marks]

tol_1=0
tol_5=0
tol_r=0

resistance = float(input("Enter resistance (0 to Exit): "))

while resistance > 0:
    if 99 <= resistance <= 101:
        tol_1 = tol_1 + 1
    elif 95  <= resistance <= 105:
        tol_5 = tol_5 + 1
    else:
        print("Invalid resistance value.")
        
    resistance = float(input("Enter resistance (0 to Exit): "))

print("1% Tolerance: ", tol_1)
print("5% Tolerance: ", tol_5)
print("Rejected: ", tol_r)