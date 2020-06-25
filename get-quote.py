import random

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt",encoding="utf-8")
  quotes = f.readlines()
  f.close()
  last = 16
  rnd = random.randint(0, last)
  print(quotes[rnd][:-1])
  rnd = random.randint(0, last)
  print(quotes[rnd][:-1])

if __name__== "__main__":
  primary()
