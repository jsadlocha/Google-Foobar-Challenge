def solution(s):
    routes = ''.join(s.split('-')).split()[0]
    res = 0
    for i, r in enumerate(routes):
        if r == '>':
            for j in routes[i+1:]:
                if r != j:
                    res += 1
        else:
            for j in routes[0:i]:
                if r != j:
                    res += 1
    return res

assert solution(">----<") == 2
assert solution("<<>><") == 4
assert solution("--->-><-><-->-") == 10

