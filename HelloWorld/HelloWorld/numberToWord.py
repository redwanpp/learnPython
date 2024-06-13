digits_mapping = {
    '0': 'zero',
    '1': 'one',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

phone = input('Phone: ')
output = ''

for ch in phone:
    output += digits_mapping.get(ch, '!') + ' '

print(output)