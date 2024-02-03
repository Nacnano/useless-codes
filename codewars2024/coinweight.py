# instagram (me and my friends)
# moosa.tae
# chotpipsit.nac
# rufflogix
# teamangkorn

f = open("codewars2024/text.txt", "r")
ret = 0
lines = []
for line in f.read():
    lines += [line]


dp = [0] * 1100

dp[85] = 1
dp[60] = 1
dp[40] = 1
dp[30] = 1

for add in [30, 40, 60, 85]:
    for i in range(1000):
        dp[i+add] +=  dp[i]


def rec(w):
    global ret
    # if w == 0:
    if w in [30,40,60,85]:
        # ret += 1
        return 0
    if w <0:
        return
    
    rec(w-85)
    rec(w-60)
    rec(w-40)
    rec(w-30)

rec(555)
print(ret)
print(dp[555])