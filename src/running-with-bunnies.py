from collections import deque
import numpy as np

def calc_shortest_path(mtx):
    arr = mtx
    any_changes = True
    while any_changes:
      any_changes = False
      for i, r in enumerate(arr):
          for j, c in enumerate(r):
              if i == j:
                continue
              base_row = np.array(arr[i])
              calc_row = np.array(arr[j])
              minimum = np.minimum(calc_row + c, base_row)
              if not np.array_equal(base_row, minimum):
                any_changes = True
                arr[i] = minimum.tolist()
    return arr

def is_possible_to_escape(row, time):
    if (time - row[-1]) > -1:
        return True
    return False

def solution(times, times_limit):
    col_size = len(times[0])

    arr = calc_shortest_path(times)

    que = deque()
    for i, r in enumerate(arr):
      for j, c in enumerate(r):
        if i == j and c == 0:
            continue
        visited = set()
        que.append((j, times_limit-c, visited))
      break

    bunnies = col_size-2
    best = []
    while que:
        r_idx, time_left, vis = que.pop()

        if r_idx > 0 and r_idx < (col_size-1):
          vis.add(r_idx-1)

        if not is_possible_to_escape(arr[r_idx], time_left):
          continue

        if len(vis) > len(best):
          best = vis
        elif len(vis) == len(best):
          best = np.minimum(np.array(list(vis)), np.array(list(best))).tolist()

        if len(best) == bunnies:
           break

        for i, col in enumerate(arr[r_idx]):
          if i == r_idx and col == 0:
             continue
          if (i-1) in vis:
             continue
          if i == bunnies or i == 0 and col > -1:
              continue
          que.appendleft((i, time_left-col, vis.copy()))

    return list(best)

assert solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1) == [1, 2]
assert solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3) == [0, 1]

