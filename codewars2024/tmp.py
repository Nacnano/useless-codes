ret = 0

n = 5

ls = [[" "]* 11] * 11

for i in range(2*n):
    ls[0][i] = "-"
    ls[n-1][i] = '-'
    ls[i][0] = "|"
    ls[i][n-1] = "|"

    ls[i][i] = "\\"
    ls[n-i-1][i] = "/"


for i in range(3):
    for j in range(3):
        ls[i*n][j*n] ="+"

for i in range(2*(n-1)):
    for j in range(2*(n-1)):
        print(ls[i][j], end="")
    print()







print(ret)