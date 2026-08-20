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

def count_pairs(corpus):
    pares = {}
    for palabra in corpus:
        for i in range(len(palabra)-1):
            par = (palabra[i], palabra[i+1])
            if par in pares:
                pares[par]+=1
            else:
                pares[par]=1
    return pares

paresA = sorted(
    count_pairs(tokensA).items(),
    key=lambda x: x[1],
    reverse=True
)

paresB = sorted(
    count_pairs(tokensB).items(),
    key=lambda x: x[1],
    reverse=True
)
print ("10 pares mas frecuentes para Corpus A:")
for par, frecuencia in paresA[:10]:
    print(par, "->", frecuencia)

print ("10 pares mas frecuentes para Corpus B:")
for par, frecuencia in paresB[:10]:
    print(par, "->", frecuencia)