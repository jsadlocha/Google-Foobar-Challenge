def solution(x, y):
    x = int(x)
    y = int(y)

    count = 0
    diff = 0
    while True:
        if x == 1 and y == 1:
            break

        if x < 1 or y < 1 or x == y:
            return str('impossible')

        if x > y:
            mod = x % y
            diff = x//y
            diff = diff-1 if mod == 0 else diff
            x -= y*diff
        else:
            mod = y % x
            diff = y//x
            diff = diff-1 if mod == 0 else diff
            y -= x*diff

        count += diff

    return str(count)

assert solution('4', '7') == '4'
assert solution('2', '1') == '1'
assert solution('1', '1') == '0'
assert solution('2', '4') == 'impossible'

