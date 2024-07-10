with open('sample.txt', 'r') as f:
    lines = f.readlines()
print(lines)

with open('sample2.txt', 'w') as f:
    f.write('test\n')

with open('sample2.txt', 'a') as f:
    f.write('test2\n')

with open('sample.txt', 'r') as f:
    for line in f:
        print(line.strip())
