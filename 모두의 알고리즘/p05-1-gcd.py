def greatest_common_divisor(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i - 1


print(greatest_common_divisor(1, 5))
print(greatest_common_divisor(3, 6))
print(greatest_common_divisor(60, 24))
print(greatest_common_divisor(81, 27))