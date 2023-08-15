from decimal import Decimal, getcontext
# beatty sequence
# S(m.sqrt(2), n) = (n + n_) * (n + n_ + 1) / 2 - S(2 + m.sqrt(2), n_)

def solution(s):
    # Beatty Sequence
    n = int(s)
    if n < 1:
        return 0

    getcontext().prec = 101
    alfa = Decimal(2).sqrt() - 1
    res = 0
    flip = False
    while n > 0:
        n_ = int(alfa * n)
        S = (n*n_ + (n*(n + 1))/2 - n_*(n_ + 1)/2)
        res = res-S if flip else res+S
        flip = not flip
        n = n_
    return str(int(res))

assert solution('5') == '19'
assert solution('77') == '4208'
# print(solution(10**105))

