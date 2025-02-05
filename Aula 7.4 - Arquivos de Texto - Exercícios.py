1.   import os

# Solicitar uma frase do usuário
frase = input("Digite uma frase: ")

# Salvar a frase em um arquivo chamado "frase.txt"
with open("frase.txt", "w") as file:
    file.write(frase)

# Obter o caminho completo do arquivo
caminho_completo = os.path.abspath("frase.txt")
print(f"Frase salva em {caminho_completo}")




2.  import re

# Ler o conteúdo do arquivo "frase.txt"
with open("frase.txt", "r") as file:
    conteudo = file.read()

# Remover caracteres não alfabéticos e separar palavras
palavras = re.findall(r'\b\w+\b', conteudo)

# Salvar as palavras, uma por linha, em "palavras.txt"
with open("palavras.txt", "w") as file:
    for palavra in palavras:
        file.write(palavra + "\n")

# Exibir o conteúdo de "palavras.txt"
with open("palavras.txt", "r") as file:
    print(file.read())




3.  # Abrir o arquivo "estomago.txt" e realizar as operações
with open("estomago.txt", "r", encoding="utf-8") as file:
    linhas = file.readlines()

# Imprimir as primeiras 25 linhas
print("Primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

# Número de linhas do arquivo
num_linhas = len(linhas)
print(f"\nNúmero de linhas no arquivo: {num_linhas}")

# Linha com o maior número de caracteres
linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com mais caracteres: {linha_mais_longa.strip()}")

# Contar menções a "Nonato" e "Íria" (ignorando maiúsculas/minúsculas)
nonato_count = sum(1 for linha in linhas if re.search(r'\bnonato\b', linha, re.IGNORECASE))
iria_count = sum(1 for linha in linhas if re.search(r'\bíria\b', linha, re.IGNORECASE))
print(f"\nMenções ao personagem Nonato: {nonato_count}")
print(f"Menções ao personagem Íria: {iria_count}")




4.   import random

# Ler palavras do arquivo "gabarito_forca.txt"
with open("gabarito_forca.txt", "r") as file:
    palavras = [linha.strip() for linha in file.readlines()]

# Escolher uma palavra aleatoriamente
palavra_secreta = random.choice(palavras)

# Ler estágios do enforcado
with open("gabarito_enforcado.txt", "r") as file:
    estagios = file.read().split("\n\n")

# Função para imprimir o enforcado
def imprime_enforcado(erros):
    print(estagios[erros])

# Inicializar jogo
letras_adivinhadas = ["_"] * len(palavra_secreta)
erros = 0
tentativas_max = 6

# Loop do jogo
while erros < tentativas_max and "_" in letras_adivinhadas:
    print(" ".join(letras_adivinhadas))
    letra = input("Adivinhe uma letra: ").lower()

    if letra in palavra_secreta:
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                letras_adivinhadas[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

# Verificar resultado
if "_" not in letras_adivinhadas:
    print("Parabéns, você venceu!")
else:
    print("Você perdeu! A palavra era:", palavra_secreta)



5.  # Informações dos livros
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    # Adicione mais livros aqui...
]

# Criar arquivo CSV
with open("meus_livros.csv", "w") as file:
    # Escrever os títulos das colunas
    file.write("Título,Autor,Ano de publicação,Número de páginas\n")

    # Escrever as informações dos livros
    for livro in livros:
        file.write(",".join(map(str, livro)) + "\n")



6.   import csv

# Abrir arquivo CSV
with open("spotify-2023.csv", "r", encoding="latin-1") as file:
    reader = csv.reader(file)
    # Pular a primeira linha de cabeçalho
    next(reader)

    # Listar músicas mais tocadas de cada ano
    top_musicas_por_ano = {}
    for row in reader:
        track_name = row[0]
        artist_name = row[1]
        year = int(row[3])
        streams = int(row[8])

        # Considerar anos de 2012 a 2022
        if 2012 <= year <= 2022:
            if year not in top_musicas_por_ano or streams > top_musicas_por_ano[year][3]:
                top_musicas_por_ano[year] = [track_name, artist_name, year, streams]

# Imprimir a lista
print([top_musicas_por_ano[year] for year in sorted(top_musicas_por_ano)])
