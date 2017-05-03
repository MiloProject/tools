# Permet de tester les expressions régulières de la base de données
import re

def teste(regexp, phrase):
    prog = re.compile(regexp)
    if prog.match(phrase):
        print("MATCH")
    else:
        print("NOPE")

if __name__ == "__main__":
    teste(input("REGEXP > "), input("TEST > "))
