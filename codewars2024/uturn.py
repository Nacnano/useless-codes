# instagram (me and my friends)
# moosa.tae
# chotpipsit.nac
# rufflogix
# teamangkorn


ret = 0

ls = [2, 8, 10, 4, 6, 2, 10, 3, 11, 7, 8, 11, 15, 12, 5, 7, 14, 2, 7, 14, 13, 7, 5, 12, 15, 11, 4, 11, 4, 11, 10, 5, 8, 2, 14, 2, 3, 10, 9, 11, 6, 14, 1, 14, 12, 2, 9, 15, 8, 7, 3, 14, 8, 2, 12, 7, 5, 3, 10, 9, 12, 3, 8, 11, 2, 4, 10, 6, 13, 15, 4, 5, 13, 3, 6, 3, 8, 7, 4, 1, 4, 8, 6, 5, 3, 14, 10, 2, 6, 9, 3, 11, 12, 2, 1, 15, 9, 4, 13, 2]

if ls[0] % 2:
    ret +=1
    
for i in range(1, len(ls)):
    if ls[i] % 2 == ls[i-1] % 2 == 1:
        if ls[i] > ls[i-1]:
            pass
        else:
            ret +=2 
    elif ls[i] % 2 == ls[i-1] % 2 == 0:
        if ls[i] < ls[i-1]:
            pass
        else:
            ret +=2
    else:
        ret +=1


print(ret)