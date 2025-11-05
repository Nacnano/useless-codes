# X is the position of the knight on the x-axis
# Y is the position of the knight on the y-axis

# Event 1 : X > 0 and X < 9 after K moves
# Event 2 : Y > 0 and Y < 9 after K moves

# Probability of increasing/decreasing 1, 2, -1, -2 in both X and Y axis is 0.25

prob_in = [[2/8, 3/8, 4/8, 4/8, 4/8, 4/8, 4/8, 3/8, 2/8], 
         [3/8, 4/8, 6/8, 6/8, 6/8, 6/8, 6/8, 4/8, 3/8],
         [4/8, 6/8, 8/8, 8/8, 8/8, 8/8, 8/8, 6/8, 4/8],
         [4/8, 6/8, 8/8, 8/8, 8/8, 8/8, 8/8, 6/8, 4/8],
         [4/8, 6/8, 8/8, 8/8, 8/8, 8/8, 8/8, 6/8, 4/8],
         [4/8, 6/8, 8/8, 8/8, 8/8, 8/8, 8/8, 6/8, 4/8],
         [4/8, 6/8, 8/8, 8/8, 8/8, 8/8, 8/8, 6/8, 4/8],
         [3/8, 4/8, 6/8, 6/8, 6/8, 6/8, 6/8, 4/8, 3/8],
         [2/8, 3/8, 4/8, 4/8, 4/8, 4/8, 4/8, 3/8, 2/8]
         ]

K = 1
answer = 0

def knight_prob(x, y, move):
    global answer
    
    if x < 0 or x > 8 or y < 0 or y > 8:
        return 0
    if move == K:
        answer += prob_in[y][x] / 8**K
        
    knight_prob(x + 1, y + 2, move + 1)
    knight_prob(x + 2, y + 1, move + 1)
    knight_prob(x + 2, y - 1, move + 1)
    knight_prob(x + 1, y - 2, move + 1)
    knight_prob(x - 1, y - 2, move + 1)
    knight_prob(x - 2, y - 1, move + 1)
    knight_prob(x - 2, y + 1, move + 1)
    knight_prob(x - 1, y + 2, move + 1)
        
knight_prob(4, 4, 0) 

print(answer)

# import math

# moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
# x = 0
# y = 0

# n = 1000000

# for i in range(n):
#     move= moves[math.random() * 8 // 1 ]
#     x += 
#     y += 
    
    
    
    
# 5 Cards
# Random a card. Expected number of draws to get all 5 cards.



# 5 * (1/1 + 1/2 + 1/3 + 1/4 + 1/5)

# 1

# 1 * 1

# 2

# 2 * (1/1 + 1/2)

# 2 * 1 + 1

# 3 * (1/1 + 1/2 + 1/3)

# 3 * 1 + 3 * (1/2) + 3 * (1/3)
