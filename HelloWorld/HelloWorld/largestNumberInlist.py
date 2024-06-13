numbers = [5, 10, 20, 6, 8, 9, 100, 99]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f'Largest number in the list is {largest}')