numbers = [5, 1, 8, 3, 8, 2]

max1 = -999999999   # very small initial value
max2 = -999999999   # second max

i = 0
while i < len(numbers):
    n = numbers[i]

    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2 and n != max1:
        max2 = n

    i += 1

print("Maximum number:", max1)
print("Second maximum number:", max2)
