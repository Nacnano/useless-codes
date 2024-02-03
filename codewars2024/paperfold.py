ret = 0

h = 210
w = 297

## sol 1
# while h > 2 or w > 2:
#     ret +=1
#     if h > w:
#         h /=2
#     else:
#         w /=2

## sol2 
while h > 2:
    h /=2
    ret +=1

while w > 2:
    w /=2
    ret +=1

print(ret)