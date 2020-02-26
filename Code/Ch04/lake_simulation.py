import random, itertools
from operator import methodcaller

class Village:
  def __init__(self):
    self.population = random.uniform(1000,5000)
    self.cheat_rate = random.uniform(.05,.15)

  def update(self, sim):
    if sim.cheaters >= 2:
      self.cheat_rate += .05
    self.population = int(self.population*1.025)

  def go_fishing(self):
    if random.uniform(0,1) < self.cheat_rate:
      cheat = 1
      fish_taken = self.population * 2
    else:
      cheat = 0
      fish_taken = self.population * 1
    return fish_taken, cheat


class Lake_Simulation:
  def __init__(self):
    self.villages = [Village() for _ in range(4)]
    self.fish = 80000
    self.year = 1
    self.cheaters = 0

  def simulate(self):
    for _ in itertools.count():
        yearly_results = map(methodcaller("go_fishing"), self.villages)
        fishs, cheats = zip(*yearly_results)
        total_fished = sum(fishs)
        self.cheaters = sum(cheats)
        if self.year > 1000:
            print("Wow! Your villages lasted 1000 years!")
            break
        if self.fish < total_fished:
            print("The lake was overfished in {} years.".format(self.year))
            break
        else:
            self.fish -= total_fished
            self.fish = self.fish*1.15
            map(methodcaller("update"), self.villages)
            print("Year {:<5}   Fish: {}".format(self.year,
                                                 int(self.fish)))
            self.year += 1

  def __iter__(self):
    self.n = 0
    return self

  def __next__(self):
    if self.n < len(self.villages):
        n = self.n
        self.n +=1
        return self.villages[n]
    else:
        raise StopIteration

if __name__ == "__main__":
    random.seed("Wolohan")
    Lake = Lake_Simulation()
    Lake.simulate()
