# Permet de tester les expressions régulières de la base de données
import re

def teste(regexp, phrase):
  if re.match(regexp, phrase):
    print("MATCH")
  else:
    print("NOPE")
    
if __nhame__ == "__main__":
  teste(input("REGEXP > "), input("TEST > "))
