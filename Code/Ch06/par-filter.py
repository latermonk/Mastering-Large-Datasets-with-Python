from functools import reduce

def map_combination(left, right):
  return left + right

def keep_if_even(acc, nxt):
    if nxt % 2 == 0:
        return acc + [nxt]
    else: return acc

xs = [1,2,3,4]
ys = [5,6,7,8]
zs = [9,10,11,12]

f_acc = keep_if_even
f_com = map_combination

res_x = reduce(f_acc, xs, [])
res_y = reduce(f_acc, ys, [])
res_z = reduce(f_acc, zs, [])

print(f_com(f_com(res_x, res_y), res_z))
