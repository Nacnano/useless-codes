ret = 0

list = [-54, 39, -2, -88, 42, -18, -16, -16, 0, 22, 70, 55, -57, 43, -27, 88, 28, 6, 60, -39, -85, 46, -57, 83, 0, -53, 0, 10, 22, -78, 26, -7, 100, -87, 47, 72, 94, -11, -42, 100, 63, -35, 39, 2, 57, -30, -17, -75, 27, 83]


for i in range(len(list)):
    for j in range(i+1, len(list)+1):
        sum = 0
        for k in range(i, j):
            sum += list[k]
        ret = max(ret, sum)

print(ret)