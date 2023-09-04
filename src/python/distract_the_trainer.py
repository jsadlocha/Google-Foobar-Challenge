from fractions import gcd

def solution(banana_list):
    class Node():
        def __init__(self, val):
            self.val = val
            self.edges = []
            self.pair = None

    def is_pair_playing_inf(p):
        l, r = p
        if l == r:
            return False

        v = (l+r)//gcd(l,r)
        return bool(v & (v-1))

    def find_augmented_path(iter):
        queue, even = iter
        end = False
        while queue:
            q, p, v = queue.pop()
            end = False
            for n in q.edges:
                if n in v:
                    continue
                if n in unpaired:
                    end = True
                    return p+[n], (queue, even)
                n_n = n.pair
                if (even and n_n is not None) or (not even and n_n is None):
                    v.add(n)
                    queue.append((n_n, p+[n,n_n], v)) # bfs
                    # queue.insert(0,(n_n, p+[n,n_n], v)) # dfs

                if end:
                    break
            if end:
                break
            even ^= True
        return None, None


    def create_iterator(i):
        iter = dict({'d':([(i, [i], set([i]))], True)})

        def iterator():
            if iter['d'] is None:
                return None

            path, iter['d'] = find_augmented_path(iter['d'])
            return path

        return iterator

    arr = banana_list[:]
    arr = [Node(i) for i in arr]

    for i in arr:
        tmp = arr[:]
        tmp.pop(tmp.index(i))
        for j in tmp:
            if is_pair_playing_inf((i.val, j.val)):
                i.edges.append(j)

    while True:
      for i in arr:
        if i.pair is not None:
            continue

        for j in i.edges:
            if j.pair is not None:
                continue
            i.pair = j
            j.pair = i
            break

      paired_list = [x.pair for x in arr]
      result = paired_list.count(None)
      if result < 2:
          return result

      unpaired = list(filter(lambda x: True if x not in paired_list else False, arr))

      found = False
      for i in unpaired:
          if i.pair is not None:
              continue
          it = create_iterator(i)
          path = it()
          if path is None:
              break

          found = True
          for l, r in zip(path[::2], path[1::2]):
            l.pair = r
            r.pair = l
          break

      if not found:
          break

    return result

assert solution([0]) == 1
assert solution([0, 0]) == 2
assert solution([1]) == 1
assert solution([1,1]) == 2
assert solution([1,1,1]) == 3
assert solution([1,1,1,1]) == 4
assert solution([1,4]) == 0
assert solution([4, 8]) == 0
assert solution([1,1,1,2]) == 2
assert solution([1,1,1,1,2,2,4]) == 1
assert solution([1,2,3,4,5,6,7,8,9,10]) == 0
assert solution([2,5,4,7,9,11]) == 0
assert solution([1,2,3]) == 1
assert solution([3,19,21,1,13,7]) == 0
assert solution([1,7,3,21,13,19]) == 0
assert solution([i+10000000 for i in range(1, 1000)]) == 1

