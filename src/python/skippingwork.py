def solution(x, y):
    return list(set(x).symmetric_difference(y))[0]

assert solution([1,2,3,4], [1,3,4]) == 2
