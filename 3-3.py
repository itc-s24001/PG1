my_list = [0, 1, 4, 9, 16, 25, 36]
for i in my_list:
    if i % 2 == 0:
        print(i)
    elif i % 2 == 1:
        print(i)

my_list = ['tokyo', 'osaka', 'fukuoka', 'aichi', 'kyoto', 'chiba', 'saitama', 'gunma']
my_list6 = []
for s in my_list:
    if len(s) >= 6:
        my_list6.append(s)
print(my_list6)
