import numpy as np
from fractions import Fraction

def solution(m):
    matrix = np.array(m)

    error = [1]+[0]*(len(m)-1)+[1]
    if np.sum(matrix[0]) == 0:
        return error
    m_sum = np.sum(matrix, axis=1)

    normal_states = np.argwhere(m_sum).reshape(-1)
    terminate_states = np.argwhere(m_sum == 0).reshape(-1)

    if len(terminate_states) == 0:
        return [0]

    def to_frac(x): return Fraction(x).limit_denominator(50)

    def print_frac(x): return x.__str__()

    matrix = matrix.astype('float')
    states = matrix[normal_states]
    s = np.sum(states, axis=1)
    prob = (states.T/s).T

    matrix[normal_states] = prob

    IORQ_state_order = np.hstack([terminate_states, normal_states])
    IORQ_order_recover = np.argsort(IORQ_state_order)
    IORQ_matrix = matrix[IORQ_state_order, :][:, IORQ_state_order]

    st = np.arange(matrix.shape[0])
    num_normal_states = len(normal_states)
    num_terminate_states = len(terminate_states)

    I_eye = np.eye(num_terminate_states)
    IORQ_matrix[:num_terminate_states, :num_terminate_states] = I_eye

    I = IORQ_matrix[:num_terminate_states, :num_terminate_states]
    O = IORQ_matrix[:num_terminate_states, num_terminate_states:]
    R = IORQ_matrix[num_terminate_states:, :num_terminate_states]
    Q = IORQ_matrix[num_terminate_states:, num_terminate_states:]

    Q_clear = np.zeros(Q.shape)
    I = np.eye(Q.shape[0])
    F = np.linalg.inv(I-Q)
    F = np.vectorize(to_frac)(F)
    FR = np.dot(F, R)
    FR = np.vectorize(to_frac)(FR)

    def den(x): return x.denominator
    def num(x): return x.numerator

    an = np.vectorize(num)(FR[0])
    ad = np.vectorize(den)(FR[0])

    lcm = np.lcm.reduce(ad)

    normalize = lcm/ad
    result = an * normalize
    result = np.hstack([result, lcm])

    return list(result)


inp1 = [
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
# [7, 6, 8, 21]

inp2 = [
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
# [0, 3, 2, 9, 14]

matrix = [
    # s0, the initial state, goes to s1 and s5 with equal probability
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],  # s1 can become s0, s3, or s4, but with different probabilities
    # s2 is terminal, and unreachable (never observed in practice)
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],  # s3 is terminal
    [0, 0, 0, 0, 0, 0],  # s4 is terminal
    [0, 0, 0, 0, 0, 0],  # s5 is terminal
]

m = [
    [0, 1, 1, 2],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

zz = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0],
]

assert solution(matrix) == [0, 3, 2, 9, 14]
assert solution(inp1) == [7, 6, 8, 21]
assert solution(inp2) == [0, 3, 2, 9, 14]
assert solution(zz) == [0]
assert solution([[0, 1], [0, 0]]) == [1,1]
assert solution([[1, 1], [0, 0]]) == [1,1]

