import unicodedata

with open("Corpus A.txt", "r", encoding="utf-8") as textoA, \
     open("Corpus B.txt", "r", encoding="utf-8") as textoB:
    corpusA = textoA.read()
    corpusB = textoB.read()

corpusB = unicodedata.normalize("NFC", corpusB)

corpusA = corpusA.split()
corpusB = ''.join(c for c in corpusB if c.isalpha() or c.isspace()).split()

vocabularioInicialA = set()
vocabularioInicialB = set()

for palabra in corpusA:
    vocabularioInicialA.update(palabra)

for palabra in corpusB:
    vocabularioInicialB.update(palabra)

print("cantidad de palabras Corpus A: ", len(corpusA))
print("cantidad de palabras Corpus B: ", len(corpusB))
print("vocabulario inicial Corpus A: ", vocabularioInicialA)
print("vocabulario inicial Corpus B: ", vocabularioInicialB)

def tokenizar_palabra(palabra):
    tokens = list(palabra)
    tokens.append("</w>")
    return tokens

tokensA = []
tokensB = []

for palabra in corpusA:
    tokensA.append(tokenizar_palabra(palabra))

for palabra in corpusB:
    tokensB.append(tokenizar_palabra(palabra))

print("palabras Corpus A: ", tokensA)
print("palabras Corpus B: ", tokensB)