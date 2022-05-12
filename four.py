from collections import Counter
array_var = [
             [10, 20, 0, 40, 50, 0, 70, 80],
             [20, 10, 0, 26, 13, 0, 15, 16],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [40, 26, 0, 28, 29, 0, 31, 32],
             [50, 34, 0, 29, 37, 0, 39, 40],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [70, 50, 0, 31, 53, 0, 55, 56],
             [80, 58, 0, 32, 61, 0, 63, 65]
             ]


for i in array_var:
    cnt = Counter(i)
    if cnt[0] == len(i):
        array_var.remove(i)


new_list = []
for i in range(8):
    int_list = []
    for j in array_var:
        int_list.append(j[i])
    new_list.append(int_list)

for i in new_list:
    cnt = Counter(i)
    if cnt[0] == len(i):
        new_list.remove(i)

array_var.clear()
for i in range(len(new_list)):
    int_list = []
    for j in new_list:
        int_list.append(j[i])
    array_var.append(int_list)

print(array_var)

