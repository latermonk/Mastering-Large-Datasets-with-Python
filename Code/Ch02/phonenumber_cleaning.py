import re

class phone_formatter:
  def __init__(self):
    self.r = re.compile(r"\d")
  def prettyFormat(self,num):
    nums = self.r.findall(num)
    area_code = "".join(nums[-10:-7])
    first_3 = "".join(nums[-7:-4])
    last_4 = "".join(nums[-4:len(nums)])
    return "({}) {}-{}".format(area_code,first_3,last_4)

if __name__ == "__main__":
  phone_numbers = [
    "(123) 456-7890",
    "1234567890",
    "123.456.7890",
    "+1 123 456-7890"
  ]

  P = phone_formatter()

  print(list(map(P.prettyFormat,phone_numbers)))
