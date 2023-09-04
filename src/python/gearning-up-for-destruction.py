def solution(pegs):
    if len(pegs) < 2 or len(pegs) > 20:
        return -1, -1

    if len(pegs) == 2:
        d = pegs[1] - pegs[0]
        gear = d*3 - d

        if gear < 1 or d < 2:
            return -1, -1

        if (gear % 3) == 0:
            return gear/3, 1

        return gear, 3

    if len(pegs) > 2:
        d = [pegs[x+1]-pegs[x] for x in range(len(pegs)-1)]
        d_sum = sum([el if i % 2 == 0 else -el for i, el in enumerate(d[::-1])])
        even = len(pegs) % 2 == 0


        first_gear = d_sum
        last_gear = float(d_sum)/3 if even else -d_sum

        gear = last_gear
        list_gears = [gear]
        for el in d[::-1]:
            gear = el - gear
            list_gears.append(gear)

        list_gears = list_gears[::-1]

        sum_gears = [list_gears[i] + list_gears[i+1] for i in range(len(list_gears)-1)]

        if sum_gears != d or min(list_gears) < 2 or min(d) < 2:
            return -1, -1

        for i in range(len(list_gears)-1):
            if (list_gears[i]+1 >= d[i]) or list_gears[i+1] >= d[i]:
                return -1, -1

        next_gear = 2*last_gear
        for el in d:
            next_gear = el-next_gear
            if next_gear < 1 or next_gear > el:
                return -1, -1

        if even:
            if d_sum % 3 == 0:
                first_gear /= 3
                return 2*first_gear, 1
            return 2*first_gear, 3

        return -2*first_gear, 1

a = [4, 30, 50]
b = [4, 17, 50]
c = [5, 30, 50, 60]
d = [10, 30, 45, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 355]

assert solution(a) == (12, 1)
assert solution(b) == (-1, -1)
assert solution(c) == (10, 1)
assert solution(d) == (10, 1)

