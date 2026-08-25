with open("Corpus A.txt", "r", encoding="utf-8") as corpus:
    corpusA = corpus.read()

cantidadDePalabras = len(corpusA.split())
vocabularioInicial = set(corpusA.split())

print(cantidadDePalabras)
print(vocabularioInicial)
