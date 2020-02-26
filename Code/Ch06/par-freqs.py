from functools import reduce

def combine_counts(left, right):
  unique_keys = set(left.keys()).union(set(right.keys()))
  return {k:left.get(k,0)+right.get(k,0) for k in unique_keys}

def make_counts(acc, nxt):
    acc[nxt] = acc.get(nxt,0) + 1
    return acc


xs = "miss"
ys = "iss"
zs = "ippi"

f_acc = make_counts
f_com = combine_counts

res_x = reduce(f_acc, xs, {})
res_y = reduce(f_acc, ys, {})
res_z = reduce(f_acc, zs, {})

print(f_com(f_com(res_x, res_y), res_z))
