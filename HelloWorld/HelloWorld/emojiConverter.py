emojies = {
    ':)': '😀',
    ':(': '😔',
    '-_-': '😑'
}

message = input('> ')
words = message.split(' ')
output = ''

for word in words:
    output += emojies.get(word, word) + ' '
print(output)