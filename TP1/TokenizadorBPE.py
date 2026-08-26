from collections import Counter

#Parte 1 – Preparación del Corpus
with open("Corpus A.txt", "r", encoding="utf-8") as corpus:
    corpusA = corpus.read()

cantidadDePalabras = len(corpusA.split())
vocabularioInicial = set(corpusA.split())

#print(cantidadDePalabras)
#print(vocabularioInicial)

#Parte 2 – Tokenización Inicial
corpusATokenizado = [letra for palabra in corpusA.split() for letra in list(palabra) + ["</w>"]]
conjuntoDeTokens = set(corpusATokenizado)

#print(corpusATokenizado)

#Parte 3 – Conteo de Frecuencias
def count_pairs(corpus):
    todos = zip(corpus, corpus[1:])
    pares = [
        par for par in todos
        if not par[0].endswith('</w>')
    ]
    return "\n".join([f"{par} -> {frecuencia}" for par, frecuencia in Counter(pares).most_common(10)])

print(count_pairs(corpusATokenizado))

#Parte 4 – Primera Fusión BPE
max_item = 22
nuevoCorpusA = corpusATokenizado.copy()

def generar_nuevo_corpus(corpus, par_mas_repe, par_fusionado):
    fst, snd = par_mas_repe
    for i in range(len(corpus) - 2, -1, -1):
        if corpus[i] == fst and corpus[i + 1] == snd:
            corpus[i] = par_fusionado
            del corpus[i + 1]

for i in range(max_item):
    par_mas_repe = eval(count_pairs(nuevoCorpusA).split('\n')[0].split(' -> ')[0])
    par_fusionado = "".join(par_mas_repe)
    conjuntoDeTokens.add(par_fusionado)
    generar_nuevo_corpus(nuevoCorpusA, par_mas_repe, par_fusionado)

print(conjuntoDeTokens)
print(corpusATokenizado)
print(nuevoCorpusA)