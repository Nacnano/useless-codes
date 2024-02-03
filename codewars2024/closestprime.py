ret = 0

def isPrime(x):
    for i in range(2, int(x **0.5)):
        if x % i == 0:
            return False
    return True

x = 123456 
ls = []
for i in range(2, 2*x):
    if isPrime(i):
        ls += [[abs(x-i), i]]

ls.sort()

mn = []
for i in ls[:3]:
    mn += [i[1]]

print(sum(mn))