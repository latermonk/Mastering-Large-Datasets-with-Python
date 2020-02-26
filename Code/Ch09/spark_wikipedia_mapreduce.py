#! /usr/bin/env python3
import re, json
from math import log2, log10, ceil
from functools import partial
from pyspark import SparkContext

def ceil5(x):
    return ceil(x/5)*5

def get_winner_loser(match):
  ms = match.split(',')
  # Put the loser in first position, winner in second
  return (ms[20], ms[10])

def initialize_voting(losses):
    return {'losses': losses,
            'n_losses': len(losses),
            'rating': 100}

def empty_ratings(d):
  d['rating'] = 0
  return d

def allocate_points(acc, nxt, i):
  k,v = nxt
  if i == 0:
    boost = 100 / (v['n_losses']+.01)
  else:
    boost = v['rating'] / (v['n_losses'] + .01)
  for loss in v['losses']:
    if loss not in acc.keys():
      acc[loss] = {'losses':[], 'n_losses': 0}
    opp_rating = acc.get(loss,{}).get('rating',0)
    acc[loss]['rating'] = opp_rating + boost
  return acc

def combine_scores(a, b):
  for k,v in b.items():
    try:
      a[k]['rating'] = a[k]['rating'] + b[k]['rating']
    except KeyError:
      a[k] = v
  return a

if __name__ == "__main__":
  sc = SparkContext(appName="WikiMap")
  entries = sc.textFile("wikipedia_edges.txt")
  xs = entries.flatMap(lambda x:x.split('\n'))\
                 .map(lambda x:x.split('\t'))\
                 .groupByKey()\
                 .mapValues(initialize_voting)

  for i in range(7):
    if i > 0:
      xs = sc.parallelize(zs.items())
    acc = dict(xs.mapValues(empty_ratings).collect())
    agg_f = partial(allocate_points, i=i)
    zs = xs.aggregate(acc, agg_f, combine_scores)

  ratings = [(k,v['rating']) for k,v in zs.items()]
  for player, rating in sorted(ratings, key=lambda x: x[1], reverse=True)[:50]:
    print('{:<30}{}\t{}'.format(player,
                                round(log2(rating+1), 1),
                                ceil5(rating)))
