# A2.py | Current Direction   [5 marks] 

current = float(input("Enter current (A): "))
if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")