import random
def plop():
   #print("Keep it logically awesome.")

  f = open("quotes.txt", "r+")
  str1 = "Not All Those Who Wander Are Lost\n"
  f.write(str1)
  quotes = f.readlines()
  f.close()
  last = len(quotes)

  randomQuote = random.randint(0, last)
  print(quotes[randomQuote])
  randomQuote = random.randint(0, last)
  print(quotes[randomQuote])
  print(quotes[14])
  print(quotes[last])
  print(quotes)
  print(last)
if __name__== "__main__":
  plop()
