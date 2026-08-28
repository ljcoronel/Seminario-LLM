import re
import time
from collections import Counter
import unicodedata

nombre_archivo_entrenamiento = input('Archivo de entrenamiento:')
nombre_archivo_inferencia = input('Archivo de inferencia:')
cant_iteraciones = int(input('Cantidad de iteraciones:'))

with open(nombre_archivo_entrenamiento, "r", encoding="utf-8") as corpus:
    corpus = " ".join(re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+', (unicodedata.normalize('NFC', corpus.read())))).lower().split()

with open(nombre_archivo_inferencia, "r", encoding="utf-8") as texto:
    texto = " ".join(re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+', (unicodedata.normalize('NFC', texto.read())))).lower().split()

def tokenizar(corpus):
    corpus_tokenizado = []
    for palabra in corpus:
        corpus_tokenizado.extend(palabra)
        corpus_tokenizado.append('</w>')
    return corpus_tokenizado

def count_pairs(corpus):
    pares = Counter()
    for i in range(len(corpus)-1):
        fst = corpus[i]
        snd = corpus[i+1]
        if not fst.endswith('</w>'):
            pares[(fst,snd)] += 1
    return pares

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

def fusion(corpus, conjunto_tokens, historial_fusiones, max_item):
    for i in range(max_item):
        pares = count_pairs(corpus)
        if not pares:
            break
        par_mas_repe = pares.most_common(1)[0][0]
        conjunto_tokens.add(par_mas_repe[0] + par_mas_repe[1])
        historial_fusiones.append((i + 1, par_mas_repe))
        corpus = actualizar(corpus, par_mas_repe)
    return corpus

def inferir(texto, historial_fusiones):
    for i, par in historial_fusiones:
        texto = actualizar(texto, par)
    return texto

cant_palabras = len(corpus)
vocabulario_inicial = set(corpus)
corpus = tokenizar(corpus)
conjunto_tokens = set(corpus)
cant_inicial_token = len(conjunto_tokens)
historial_fusiones = []
inicio = time.perf_counter()
nuevo_corpus = fusion(corpus.copy(), conjunto_tokens, historial_fusiones, cant_iteraciones)
fin = time.perf_counter()
cant_final_token = len(conjunto_tokens)
texto = inferir(tokenizar(texto), historial_fusiones)

print('Cantidad de palabras:', cant_palabras)
print('Vocabulario inicial:', vocabulario_inicial)
print('Palabras del corpus antes:',corpus)
print('10 pares más frecuentes')
for par, frecuencia in count_pairs(corpus).most_common(10):
    print(f"{par} -> {frecuencia}")
print('Pares fusionados:')
for i, par in historial_fusiones:
    print(f"{i} : {par}")
print('Palabras del corpus después:', nuevo_corpus)
print('Cantidad inicial de tokens:', cant_inicial_token)
print('Cantidad final de tokens:', cant_final_token)
print('Tamaño del vocabulario:', len(set(nuevo_corpus)))
print('Cantidad promedio de tokens por palabra:', len(nuevo_corpus)/cant_palabras)
print('Tiempo de entrenamiento:', fin-inicio)
print('Tokenizar nuevas palabras:', texto)