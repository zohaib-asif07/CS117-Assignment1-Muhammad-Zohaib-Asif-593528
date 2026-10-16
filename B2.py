# B2.py | Resistors in Series   [5 marks]

count = int(input("How many resistors? "))
total = 0

for i in range(1, count + 1):
    resistance = float(input("Enter resistance: "))
    total = total + resistance

print("Total resistance =", total, "ohm")