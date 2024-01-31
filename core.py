import re
from builtins import enumerate

import yaml
from PyPDF2 import PdfReader


def extrair_texto_de_pdf(caminho_do_pdf):
    texto = ''
    with open(caminho_do_pdf, 'rb') as arquivo_pdf:
        leitor_pdf = PdfReader(arquivo_pdf)
        num_paginas = len(leitor_pdf.pages)

        for pagina_num in range(num_paginas):
            pagina = leitor_pdf.pages[pagina_num]
            texto += pagina.extract_text()

    return texto


def encontrar_estrutura(texto, padrao):
    linhas = texto.split('\n')
    matches = [(i, linha) for i, linha in enumerate(linhas) if re.search(padrao, linha)]
    return matches


padrao_procurado = r"Sentences to study"  # Padrão que você deseja procurar no texto

# Substitua 'caminho/do/seu/arquivo.pdf'

with open('local.yml', 'r', encoding='utf-8') as file:
    dados = yaml.safe_load(file)
print(dados['local'])

caminho_do_pdf = dados['local']
texto_extraido = extrair_texto_de_pdf(caminho_do_pdf)
print(texto_extraido)

resultados = encontrar_estrutura(texto_extraido, padrao_procurado)
if resultados:
    print("Estrutura encontrada nos seguintes locais:")
    for indice, linha in resultados:
        print(f" Linha {indice + 1}: {linha}")
else:
    print("Estrutura não encontrada no texto do PDF.")
