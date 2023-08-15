import math as m
from collections import deque, defaultdict, Counter

def generate_2x2():
    backward = {0: set(), 1:set()}
    bw1up = defaultdict(set)
    bw0up = defaultdict(set)
    pow2 = { 2**x for x in range(4)}
    for i in range(0, 2**4):
        if1or0 = 1 if i in pow2 else 0
        convert = tuple((i >> x) & 1 for x in range(4) )
        backward[if1or0].add(convert)
        dict_ = bw1up if if1or0 else bw0up
        up = convert[:2]
        dict_[up].add(convert)

    return backward, bw1up, bw0up

def generate_preimgs_col(uni_col, ncols, cols):
    bw, b1up, b0up = generate_2x2()
    col_dict = { x: [] for x in uni_col}
    fw_preimg = defaultdict(list)
    bw_preimg = defaultdict(lambda: defaultdict(list))

    for i_, c in enumerate(uni_col):
        bin_ = [(c >> x) & 1 for x in range(ncols)]
        nb = len(bin_)-1

        fw_state = fw_preimg[c]
        bw_state = bw_preimg[c]

        que = deque()
        all_poss = bw[bin_[0]]
        for i in all_poss:
            que.append((i[2:], 0, i))

        while que:
            state, idx, val = que.pop()

            if idx == nb:
                b_ = sum([ x << i for i,x in enumerate(val[1::2])])
                f_ = sum([ x << i for i, x in enumerate(val[0::2])])
                bw_state[b_].append(f_)
                fw_state.append(b_)
                continue

            n_idx = idx + 1
            dict_ = b1up if bin_[n_idx] else b0up
            if state in dict_:
                que.extend((i[2:], n_idx, val+i[2:]) for i in dict_[state])

    return fw_preimg, bw_preimg

def solution(arr):
    transpoz = tuple(zip(*arr))
    ncol = len(transpoz[0])
    cols = [sum([e << idx for idx, e in enumerate(c)]) for c in transpoz]
    uniq_col = set(cols)
    fw_preimg, bw_preimg = generate_preimgs_col(uniq_col, ncol, arr)

    que = deque()
    nc = len(cols)-1
    pre = fw_preimg[cols[0]]
    uni = set(pre)
    cnt = Counter(pre)
    cache = defaultdict(int)
    for e in uni:
        que.append((e, 0, e, [(e, 0)]))

    while que:
        fw_state, idx, init, path = que.pop()

        if (fw_state, idx) in cache:
            v_ = cache[(fw_state, idx)]
            for t in path[:-1]:
                cache[t] += v_
            continue

        if idx == nc:
            for t in path:
                cache[t] += 1
            continue

        n_idx = idx+1
        last_cols = cols[n_idx]
        next_states = bw_preimg[last_cols].get(fw_state)
        if next_states:
            que.extend((state, n_idx, init, path+[(state, n_idx)]) for state in next_states)

    res = 0
    for i in uni:
        res += cnt[i] * cache[(i, 0)]

    return res

if __name__ == "__main__":
    func = solution
    assert func([[True, True], [True, True]]) == 8
    assert func([[True, False], [True, False]]) == 20
    assert func([[False, True], [True, True]]) == 10
    assert func([[False, False], [False, False]]) == 208
    assert func([[True, False, True], [False, True, False], [True, False, True]]) == 4
    assert func([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]) == 11567
    assert func([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]) == 254

