from functools import reduce

def my_add(left, right):
  return left+right

xs = [1,2,3,4]
ys = [5,6,7,8]
zs = [9,10,11,12]

sum_x = reduce(my_add, xs)
sum_y = reduce(my_add, ys)
sum_z = reduce(my_add, zs)

print(my_add(my_add(sum_x, sum_y), sum_z))
# 78
