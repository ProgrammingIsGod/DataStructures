def solution(common):
    a, b, c = common[0], common[1], common[2]

    if b - a == c - b:
        return common[-1] + (b - a)
    
    r = b // a
    return common[-1] * r
    

print(solution([2, 4, 8, 16]))