import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    """A função compara duas assinaturas de texto e retorna o grau de similaridade entre elas."""
    soma = 0
    for i in range(6):
        soma += abs(as_a[i] - as_b[i])
    return soma / 6

def calcula_assinatura(texto):
    """A função calcula a assinatura de um texto e retorna uma lista com os traços linguísticos."""
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    num_caracteres_sentencas = 0
    num_caracteres_frases = 0

    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
        num_caracteres_sentencas += len(sentenca)

    for frase in frases:
        palavras.extend(separa_palavras(frase))
        num_caracteres_frases += len(frase)

    num_palavras = len(palavras)
    tam_medio_palavra = sum(len(palavra) for palavra in palavras) / num_palavras
    type_token = n_palavras_diferentes(palavras) / num_palavras
    hapax_legomana = n_palavras_unicas(palavras) / num_palavras
    tam_medio_sentenca = num_caracteres_sentencas / len(sentencas)
    complexidade_sentenca = len(frases) / len(sentencas)
    tam_medio_frase = num_caracteres_frases / len(frases)

    return [tam_medio_palavra, type_token, hapax_legomana, tam_medio_sentenca, complexidade_sentenca, tam_medio_frase]

def avalia_textos(textos, ass_cp):
    """A função avalia uma lista de textos e uma assinatura de referência e retorna o número do texto mais similar à assinatura."""
    similaridade_minima = float('inf')
    texto_mais_similar = 0

    for i, texto in enumerate(textos):
        ass_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(ass_texto, ass_cp)

        if similaridade < similaridade_minima:
            similaridade_minima = similaridade
            texto_mais_similar = i + 1

    return texto_mais_similar
