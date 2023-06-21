import pprint

L = 10
blue_length = 3
cost_blue = 10
red_length = 5
cost_red = 80
gray_length = 2
cost_gray = 50
prev_tube = ''

def min_cost_recursive(L, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, prev_tube):
    if L == 0:
        return 0
    
    if L < 0:
        return float('inf')
    
    
    if prev_tube == 'blue':
        return cost_gray + min_cost_recursive(L - gray_length, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, 'gray')
    
    if prev_tube == 'red':
        return min(cost_red + min_cost_recursive(L - red_length, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, 'red'), cost_gray + min_cost_recursive(L - gray_length, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, 'gray'))
    
    if prev_tube == 'gray' or prev_tube == '':
        return min(cost_blue + min_cost_recursive(L - blue_length, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, 'blue'), cost_red + min_cost_recursive(L - red_length, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, 'red'), cost_gray + min_cost_recursive(L - gray_length, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, 'gray'))


print(f'recursive: {min_cost_recursive(L, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray, prev_tube)}')


def min_cost (L, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray):
    memo = [[float('inf')] * 3 for _ in range(L)]
    
    for i in range(L):            
        # print(blue_length - (i + 1))
        if (i + 1) - blue_length >= 0:
            if (i + 1) - blue_length == 0:
                memo[i][0] = cost_blue
            if (i + 1) - blue_length > 0:
                memo[i][0] = cost_blue + memo[i - blue_length][2]
        if (i + 1) - red_length >= 0:
            if (i + 1) - red_length == 0:
                memo[i][1] = cost_red
            if (i + 1) - red_length > 0:
                memo[i][1] = cost_red + min( memo[i - red_length][1], memo[i - red_length][2])
        if (i + 1) - gray_length >= 0:
            if (i + 1) - gray_length == 0:
                memo[i][2] = cost_gray
            if (i + 1) - gray_length > 0:
                memo[i][2] = cost_gray + min(memo[i - gray_length][0], memo[i - gray_length][1], memo[i - gray_length][2])

    # pprint.pprint(memo)

    return min(memo[L - 1][0], memo[L - 1][1], memo[L - 1][2])

print(f'memo: {min_cost(L, blue_length, cost_blue, red_length, cost_red, gray_length, cost_gray)}')


    