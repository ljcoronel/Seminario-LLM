#Parte 1 – Preparación del Corpus
with open("Corpus A.txt", "r", encoding="utf-8") as corpus:
    corpusA = corpus.read()

cantidadDePalabras = len(corpusA.split())
vocabularioInicial = set(corpusA.split())

print(cantidadDePalabras)
print(vocabularioInicial)

#Parte 2 – Tokenización Inicial
corpusATokenizado = [letra for palabra in corpusA.split() for letra in list(palabra) + ["</w>"]]
conjuntoDeTokens = set(corpusATokenizado)

print(corpusATokenizado)
print(conjuntoDeTokens)