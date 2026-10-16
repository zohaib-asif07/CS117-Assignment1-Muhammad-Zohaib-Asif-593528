# B3.py | Sensor Readings   [5 marks]

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

count = 0
highest = readings[0] #used as reference which will change later if condition isnt met
lowest = readings[0]
total = 0

for r in readings:
    if r > 3.2:
        count = count + 1

    if r > highest:
        highest = r

    if r < lowest:
        lowest = r

    total = total + r

average = total / len(readings)

print("Readings above 3.2 V:", count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", average, "V")