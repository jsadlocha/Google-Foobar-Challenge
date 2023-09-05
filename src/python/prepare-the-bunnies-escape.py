def solution(map):
    row_size = len(map)-1
    col_size = len(map[0])-1
    get_dir = lambda c, r, s, w: [[c, r-1, s, w], [c, r+1, s, w], [c-1, r, s, w], [c+1, r, s, w]]

    que = [(col_size, row_size, 1, False)]
    vis = {(col_size, row_size, 1): 1}

    best = 2**64-1

    while que:
        all_neigh = []
        for i in range(len(que)):
          q = que.pop()
          c, r, s, w = q

          if (c, r) == (0,0):
              best = min(best, s)

          all_neigh.append(get_dir(c, r, s, w))

        if best < (2**64-1):
          return best

        for neigh in all_neigh:
          for col, row, step, wall in neigh:
              if (col, row, wall) in vis:
                  continue

              if col > col_size or col < 0 or row > row_size or row < 0:
                  continue

              if map[row][col] == 1:
                  if wall == True:
                      continue
                  wall = True

              que.append((col,row,step+1, wall))
              vis[(col,row,wall)] = step+1
    return best

# test cases
assert solution([[0, 1, 1, 0],
          [0, 0, 0, 1],
          [1, 1, 0, 0],
          [1, 1, 1, 0]]) == 7

assert solution([[0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0]]) == 11


assert solution([[0,0,0,0,0],
                 [1,1,1,0,1],
                 [0,0,0,0,0],
                 [0,1,1,1,1],
                 [0,0,0,0,0],
                 [1,1,1,0,1],
                 [0,0,0,0,0],
                 [0,0,0,1,1],
                 [0,0,0,0,0]]) == 15

assert solution([[0,0,0,0,0,0,0,0],
                 [1,1,0,1,1,1,1,0],
                 [0,0,0,0,1,1,0,0],
                 [0,1,1,1,1,1,0,1],
                 [0,1,1,1,1,1,0,1],
                 [0,0,1,1,0,0,0,0],
                 [1,0,1,1,0,1,1,1],
                 [1,0,1,1,0,1,1,1],
                 [0,0,1,0,0,0,0,0],
                 [0,1,1,0,1,1,1,0],
                 [0,0,0,0,0,1,0,0]]) == 22
