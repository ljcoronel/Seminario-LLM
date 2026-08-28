import re
import time
from collections import Counter
import unicodedata

#Parte 1 – Preparación del Corpus
with open("Corpus A.txt", "r", encoding="utf-8") as corpus:
    corpus_a = corpus.read().split()

with open("Corpus B.txt", "r", encoding="utf-8") as corpus:
    corpus_b = " ".join(re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+', (unicodedata.normalize('NFC', corpus.read())))).split()

cantidad_de_palabras_corpus_a = len(corpus_a)
vocabulario_inicial_corpus_a = set(corpus_a)

cantidad_de_palabras_corpus_b = len(corpus_b)
vocabulario_inicial_corpus_b = set(corpus_b)

print("PARTE 1")
print("Cantidad de palabras corpus A:", cantidad_de_palabras_corpus_a)
print("Vocabulario inicial corpus A:", vocabulario_inicial_corpus_a)
print("Cantidad de palabras corpus B:", cantidad_de_palabras_corpus_b)
print("Vocabulario inicial corpus B:", vocabulario_inicial_corpus_b)

#Parte 2 – Tokenización Inicial
def tokenizar(corpus):
    corpus_tokenizado = []
    for palabra in corpus:
        corpus_tokenizado.extend(palabra)
        corpus_tokenizado.append('</w>')
    return corpus_tokenizado

corpus_a = tokenizar(corpus_a)
corpus_b = tokenizar(corpus_b)
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
print("10 pares mas frecuentes corpus B:")
for par, frecuencia in count_pairs(corpus_b).most_common(10):
    print(f"{par} -> {frecuencia}")

#Parte 4 – Primera Fusión BPE
nuevo_corpus_a_1_fusion = corpus_a.copy()
conjunto_de_tokens_1_fusion = conjunto_de_tokens.copy()
historial_1_fusion = []

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

nuevo_corpus_a_1_fusion = fusion(nuevo_corpus_a_1_fusion, conjunto_de_tokens_1_fusion, historial_1_fusion, 1)

print("PARTE 4")
print("Pares fusionados corpus A:")
for i, par in historial_1_fusion:
    print(f"{i} : {par}")
print("Corpus A antes:", corpus_a)
print("Corpus A despues:", nuevo_corpus_a_1_fusion)

#Parte 5 – Entrenamiento Completo
nuevo_corpus_a_50_fusiones = corpus_a.copy()
conjunto_de_tokens_50_fusiones = conjunto_de_tokens.copy()
historial_50_fusiones = []
nuevo_corpus_a_50_fusiones = fusion(nuevo_corpus_a_50_fusiones, conjunto_de_tokens_50_fusiones, historial_50_fusiones, 50)
cantidad_final_token = len(conjunto_de_tokens_50_fusiones)

print("PARTE 5")
print("Cantidad inicial de tokens corpus A:", cantidad_inicial_token)
print("Cantidad final de tokens corpus A:", cantidad_final_token)
print("Tamaño del vocabulario corpus A:", len(set(nuevo_corpus_a_50_fusiones)))

#Parte 6 - Diferentes iteraciones
nuevo_corpus_a_30_fusiones = corpus_a.copy()
conjunto_de_tokens_30_fusiones = conjunto_de_tokens.copy()
historial_30_fusiones = []
inicio = time.perf_counter()
nuevo_corpus_a_30_fusiones = fusion(nuevo_corpus_a_30_fusiones, conjunto_de_tokens_30_fusiones, historial_30_fusiones, 30)
fin = time.perf_counter()
cantidad_final_token = len(conjunto_de_tokens_30_fusiones)
print("PARTE 6")
print("Cantidad promedio de tokens por palabra corpus A 30 fusiones:", cantidad_de_palabras_corpus_a / cantidad_final_token)
print("Tamaño del vocabulario corpus A 30 fusiones:", len(set(nuevo_corpus_a_30_fusiones)))
print("Tiempo de entrenamiento corpus A 30 fusiones:", fin-inicio)

nuevo_corpus_a_60_fusiones = corpus_a.copy()
conjunto_de_tokens_60_fusiones = conjunto_de_tokens.copy()
historial_60_fusiones = []
inicio = time.perf_counter()
nuevo_corpus_a_60_fusiones = fusion(nuevo_corpus_a_60_fusiones, conjunto_de_tokens_60_fusiones, historial_60_fusiones, 60)
fin = time.perf_counter()
cantidad_final_token = len(conjunto_de_tokens_60_fusiones)
print("Cantidad promedio de tokens por palabra corpus A 60 fusiones:", cantidad_de_palabras_corpus_a / cantidad_final_token)
print("Tamaño del vocabulario corpus A 60 fusiones:", len(set(nuevo_corpus_a_60_fusiones)))
print("Tiempo de entrenamiento corpus A 60 fusiones:", fin-inicio)

nuevo_corpus_a_100_fusiones = corpus_a.copy()
conjunto_de_tokens_100_fusiones = conjunto_de_tokens.copy()
historial_100_fusiones = []
inicio = time.perf_counter()
nuevo_corpus_a_100_fusiones = fusion(nuevo_corpus_a_100_fusiones, conjunto_de_tokens_100_fusiones, historial_100_fusiones, 100)
fin = time.perf_counter()
cantidad_final_token = len(conjunto_de_tokens_100_fusiones)
print("Cantidad promedio de tokens por palabra corpus A 100 fusiones:", cantidad_de_palabras_corpus_a / cantidad_final_token)
print("Tamaño del vocabulario corpus A 100 fusiones:", len(set(nuevo_corpus_a_100_fusiones)))
print("Tiempo de entrenamiento corpus A 100 fusiones:", fin-inicio)

#Parte 7 – Tokenizar Nuevas Palabras
with open("Nuevas Palabras.txt", "r", encoding="utf-8") as file:
    ejemplo = tokenizar(file.read().split())

def inferir(texto, historial_fusiones):
    for i, par in historial_fusiones:
        texto = actualizar(texto, par)
    return texto

ejemplo = inferir(ejemplo, historial_100_fusiones)

print("PARTE 7")
print(ejemplo)