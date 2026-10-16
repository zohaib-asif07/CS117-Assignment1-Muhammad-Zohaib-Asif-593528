# C3.py | Decimal to Binary [10 marks]

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

print(decimal_to_binary(10))
print(decimal_to_binary(25))
print(decimal_to_binary(13))