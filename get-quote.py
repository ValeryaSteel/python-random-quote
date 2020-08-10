import random
def plop():
   #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()


  last = 13
  randomQuote = random.randint (0, last)
  print(quotes[randomQuote])
  lenQuotes = len(quotes)
  print(lenQuotes)

if __name__== "__main__":
  plop()
