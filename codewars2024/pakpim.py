import json

mx = 0
node  = 0

f = open("codewars2024/json.json")
data =json.load(f)

def rec(x, sum):
    global mx, node
    
    sum += x["id"]
    if sum > mx:
        mx = sum
        node = x["id"]

    for child in x["children"]:
        rec(child, sum)

rec(data, 0)
print(mx, node)