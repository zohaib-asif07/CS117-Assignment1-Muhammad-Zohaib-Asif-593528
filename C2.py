# C2.py | Parallel Resistance [5 marks]

def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total = total + 1 / r
    return round(1 / total, 2)

print(parallel_resistance([10, 10]))
print(parallel_resistance([100, 200, 300]))
print(parallel_resistance([20, 30, 60]))