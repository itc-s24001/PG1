prefectures = ['Hokkaido', 'Hokkaido', 'Tokyo', 'Kanagawa']
cities = ['Sapporo', 'Hakodate', 'Minato', 'Yokohama']
populations = [100, 200, 300, 400]
population_dict = {(state, city): population for state, city, population in zip(prefectures, cities, populations)}
print(population_dict)

multiplicated_xy_setdict = {frozenset([x, y]): x*y for x in range(2) for y in range(2)}
print(multiplicated_xy_setdict)

multiplicated_xy_dict = {}
I = 3
J = 3
for i in range(I):
    multiplicated_xy_dict[i] = {}
    for j in range(J):
        multiplicated_xy_dict[i][j] = i*j
print(multiplicated_xy_dict)

multiplicated_xy_dict = {i:{j:(i*j) for j in range(J)} for i in range(I)}
print(multiplicated_xy_dict)

print(multiplicated_xy_dict[2][1])

#表データの生成
data = [
    ['01', '0001', 'Male', 'Yamada', 'Tarou', 25, 'Tokyo'],
    ['01', '0002', 'Male', 'Satou', 'Takeshi', 27, 'Kanagawa'],
    ['01', '0003', 'Female', 'Tanaka', 'Yuko', 25, 'Saitama'],
    ['02', '0001', 'Male', 'Smith', 'Mike', 22, 'NewJersey'],
    ['02', '0002', 'Male', 'Turner', 'Tom', 27, 'Kansas'],
    ['02', '0003', 'Male', 'Jackson', 'David', 22, 'Florida']
]

#辞書変数生成
member_infomation = {}

#表データをレコード毎に格納する
for record in data:
    key = (record[0], record[1])
    info = record[2:]
    member_infomation[key] = info

#結果を表示する
print('number', 'infomation', sep='         ')
for key, info in member_infomation.items():
    print(key, info)
