from collections import Counter

#Parte 1 – Preparación del Corpus
with open("Corpus A.txt", "r", encoding="utf-8") as corpus:
    corpus_a = corpus.read().split()

cantidad_de_palabras = len(corpus_a)
vocabulario_inicial = set(corpus_a)

print("PARTE 1")
print("Cantidad de palabras corpus A:", cantidad_de_palabras)
print("Vocabulario inicial corpus A:", vocabulario_inicial)

#Parte 2 – Tokenización Inicial
def tokenizar(corpus):
    corpus_tokenizado = []
    for palabra in corpus:
        corpus_tokenizado.extend(palabra)
        corpus_tokenizado.append('</w>')
    return corpus_tokenizado

corpus_a = tokenizar(corpus_a)
conjunto_de_tokens = set(corpus_a)
cantidad_inicial_token = len(conjunto_de_tokens)

print("PARTE 2")
print("Tokenización inicial corpus A:", corpus_a)

#Parte 3 – Conteo de Frecuencias
def count_pairs(corpus):
    pares = Counter()
    for i in range(len(corpus)-1):
        fst = corpus[i]
        snd = corpus[i+1]
        if not fst.endswith('</w>'):
            pares[(fst,snd)] += 1
    return pares

print("PARTE 3")
print("10 pares mas frecuentes corpus A:")
for par, frecuencia in count_pairs(corpus_a).most_common(10):
    print(f"{par} -> {frecuencia}")

#Parte 4 – Primera Fusión BPE
nuevo_corpus_a = corpus_a.copy()
historial_fusiones = []

def actualizar(corpus, par):
    nuevo_corpus = []
    i = 0
    n = len(corpus)
    fst, snd = par
    token = fst + snd
    while i < n:
        if i < n-1 and corpus[i] == fst and corpus[i+1] == snd:
            nuevo_corpus.append(token)
            i += 2
        else:
            nuevo_corpus.append(corpus[i])
            i += 1
    return nuevo_corpus

def fusion(corpus, conjunto_de_tokens, historial_fusiones, max_item):
    for i in range(max_item):
        pares = count_pairs(corpus)
        if not pares:
            break
        par_mas_repe = pares.most_common(1)[0][0]
        conjunto_de_tokens.add(par_mas_repe[0] + par_mas_repe[1])
        historial_fusiones.append((i + 1, par_mas_repe))
        corpus = actualizar(corpus, par_mas_repe)
    return corpus

nuevo_corpus_a = fusion(nuevo_corpus_a, conjunto_de_tokens, historial_fusiones, 1)

print("PARTE 4")
print("Pares fusionados corpus A:")
for i, par in historial_fusiones:
    print(f"{i} : {par}")
print("Corpus A antes:", corpus_a)
print("Corpus A despues:", nuevo_corpus_a)

#Parte 5 – Entrenamiento Completo
nuevo_corpus_a_50_fusiones = corpus_a.copy()
historial_fusiones = []
nuevo_corpus_a_50_fusiones = fusion(nuevo_corpus_a_50_fusiones, conjunto_de_tokens, historial_fusiones, 50)
cantidad_final_token = len(conjunto_de_tokens)

print("PARTE 5")
print("Cantidad inicial de tokens corpus A:", cantidad_inicial_token)
print("Cantidad final de tokens corpus A:", cantidad_final_token)
print("Tamaño del vocabulario corpus A:", len(set(nuevo_corpus_a_50_fusiones)))

#Parte 6 - Diferentes iteraciones
