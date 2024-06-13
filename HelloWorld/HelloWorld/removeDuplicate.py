numbers = [5, 5, 6, 10, 5, 20, 6]
numbers2 = []
for number in numbers:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)