from time import clock, sleep
from multiprocessing import Pool

def times_two(x):
  return x*2+7

def lazy_map(xs):
  return list(map(times_two, xs))

def par_map(xs):
  with Pool(2) as P:
<<<<<<< HEAD
    x =  P.map(times_two, xs, 7500)
  return x

for i in range(0,10):
=======
    x =  P.map(times_two, xs)
  return x

print("{:<12} {:>5} {:>5}".format("N","Lazy","Parl"))
for i in range(0,7):
>>>>>>> Tst
  N = 10**i
  t1 = clock()
  lazy_map(range(N))
  lm_time = clock() - t1

  t1 = clock()
  par_map(range(N))
  par_time = clock() - t1
<<<<<<< HEAD
  print("""
-- N = {} --
Lazy map time:      {}
Parallel map time:  {}
""".format(N,lm_time, par_time))
=======
  print("{:<12} {:>5.2f} {:>5.2f}".format(N,lm_time, par_time))
>>>>>>> Tst
