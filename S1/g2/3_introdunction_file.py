
file = open('data.txt', encoding='utf-8-sig')
print(file.read())
file.close()

print('='*100)

file = open('data.txt', encoding='utf-8')
print(file.readline())
print(file.readline())
file.close()

print('='*100)

file = open('data.txt', encoding='utf-8')
for line in file:
    print(line, end='')
print()
file.close()

print('='*100)

with open('data.txt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')

with open('data_1.txt', 'w') as file:
    file.write('Line 1\n')

with open('data_1.txt', 'a') as file:
    file.write('Line 2')