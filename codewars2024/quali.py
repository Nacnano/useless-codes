data = {}

ret = 0


for i in range(2000, 4001, 12):
    tmp = i
    dig = 0
    while tmp>0:
        dig += tmp % 10
        tmp //= 10
    if dig == 8:
        ret +=1

print(ret)