import unicodedata

with open("Corpus A.txt", "r", encoding="utf-8") as textoA, \
     open("Corpus B.txt", "r", encoding="utf-8") as textoB:
    corpusA = textoA.read()
    corpusB = textoB.read()

corpusB = unicodedata.normalize("NFC", corpusB)

corpusA = corpusA.split()
corpusB = ''.join(c for c in corpusB if c.isalpha() or c.isspace()).split()

cantidadPalabrasA = len(corpusA)
cantidadPalabrasB = len(corpusB)

vocabularioInicialA = set()
vocabularioInicialB = set()

for palabra in corpusA:
    vocabularioInicialA.update(palabra)

for palabra in corpusB:
    vocabularioInicialB.update(palabra)

print("cantidad de palabras Corpus A: ", cantidadPalabrasA)
print("cantidad de palabras Corpus B: ", cantidadPalabrasB)
print("vocabulario inicial Corpus A: ", vocabularioInicialA)
print("vocabulario inicial Corpus B: ", vocabularioInicialB)

def tokenizar_palabra(palabra):
    tokens = list(palabra)
    tokens.append("</w>")
    return tokens

tokensA = corpusA
tokensB = corpusB
corpusA = []
corpusB = []

for palabra in tokensA:
    corpusA.append(tokenizar_palabra(palabra))

for palabra in tokensB:
    corpusB.append(tokenizar_palabra(palabra))

print("palabras Corpus A: ", corpusA)
#print("palabras Corpus B: ", corpusB)

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

paresA = count_pairs(corpusA)

paresOrdenadosA = sorted(
    paresA.items(),
    key=lambda x: x[1],
    reverse=True
)

paresB = count_pairs(corpusB)

paresOrdenadosB = sorted(
    paresB.items(),
    key=lambda x: x[1],
    reverse=True
)
print ("10 pares mas frecuentes para Corpus A:")
for par, frecuencia in paresOrdenadosA[:10]:
    print(par, "->", frecuencia)

print ("10 pares mas frecuentes para Corpus B:")
for par, frecuencia in paresOrdenadosB[:10]:
    print(par, "->", frecuencia)

def merge_pair(corpus, par):
    nuevo_corpus = []
    for palabra in corpus:
        nueva_palabra = []
        i = 0
        while i < len(palabra):
            if i < len(palabra) - 1 and (palabra[i], palabra[i + 1]) == par:
                nueva_palabra.append(palabra[i] + palabra[i + 1])
                i += 2
            else:
                nueva_palabra.append(palabra[i])
                i += 1
        nuevo_corpus.append(nueva_palabra)
    return nuevo_corpus

cantidadInicialTokens = sum(len(palabra) for palabra in corpusA)

merges = []

for i in range(50):
    pares = count_pairs(corpusA)

    if not pares:
        break

    par_mas_frecuente = max(pares, key=pares.get)

    merges.append(par_mas_frecuente)

    corpusA = merge_pair(corpusA, par_mas_frecuente)


cantidadFinalTokens = sum(len(palabra) for palabra in corpusA)

vocabularioFinal = set()

for palabra in corpusA:
    vocabularioFinal.update(palabra)


print("\nHistorial de fusiones:")
for i, par in enumerate(merges, start=1):
    print(i, ".", par)

print("\nCantidad inicial de tokens:", cantidadInicialTokens)
print("Cantidad final de tokens:", cantidadFinalTokens)
print("Tamaño del vocabulario:", len(vocabularioFinal))
