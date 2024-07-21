x = 100
y = 100
k = 10000

def trade(asset, amount):
    global x, y, k
    
    if asset == "X":
        if amount > x:
            return "Trade rejected: Not enough reserve of asset X."
        x -= amount
        y = k / x
    elif asset == "Y":
        if amount > y:
            return "Trade rejected: Not enough reserve of asset Y."
        y -= amount
        x = k / y
    else:
        return "Trade rejected: Invalid asset."
    
    if x <= 0 or y <= 0:
        return "Trade rejected: Resulting reserves would be zero or less."
    
    return f"Trade successful. New reserves: X = {x}, Y = {y}"


trade("X", 10)

print(x, y)