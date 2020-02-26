from mrjob.job import MRJob

class WebpageAnalysis(MRJob):

  def mapper(self, _, line):
      yield line.split(',')[7], 1

  def reducer(self, key, vals):
    yield key, sum(vals)

if __name__ == "__main__":
  WebpageAnalysis.run()

