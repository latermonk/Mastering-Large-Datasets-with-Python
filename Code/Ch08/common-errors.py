from mrjob.job import MRJob

class WebpageAnalysis(MRJob):

  def mapper(self, _, line):
    fields = line.split(',')
    if fields[7] == '404.0':
      yield fields[6], 1

  def reducer(self, key, vals):
    hits = sum(vals)
    if hits>5:
      yield key, hits

if __name__ == "__main__":
  WebpageAnalysis.run()

