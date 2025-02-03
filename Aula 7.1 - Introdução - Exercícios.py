1.  def imprime_escada(nome):
    for i in range(1, len(nome) + 1):
        print(nome[:i])

nome_usuario = input("Digite seu nome: ")
imprime_escada(nome_usuario)



2.def boas_vindas(primeiro_nome, sobrenome):
    nome_completo = primeiro_nome + " " + sobrenome
    print(f"Bem-vinda, {nome_completo}!")

primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

boas_vindas(primeiro_nome, sobrenome)



3.def contar_espacos(frase):
    espacos = frase.count(" ")
    return espacos

frase = input("Digite a frase: ")
espacos_brancos = contar_espacos(frase)

print(f"Espaços em branco: {espacos_brancos}")



4. def formatar_numero(numero):
    # Verifica se o número tem 8 dígitos
    if len(numero) == 8:
        numero = "9" + numero  # Adiciona o 9 na frente
    # Verifica se o número já tem 9 dígitos e o primeiro dígito é 9
    elif len(numero) == 9 and numero[0] != "9":
        print("Número inválido. O primeiro dígito de um número de 9 dígitos deve ser 9.")
        return
    # Adiciona o separador "-" após os primeiros 5 dígitos
    numero_formatado = numero[:5] + "-" + numero[5:]
    print(f"Número completo: {numero_formatado}")

numero = input("Digite o número: ")
formatar_numero(numero)



5. def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    indices_vogais = []
    
    # Percorre a string e armazena os índices das vogais
    for i, letra in enumerate(frase):
        if letra in vogais:
            indices_vogais.append(i)
    
    # Exibe o número de vogais e os seus índices
    print(f"{len(indices_vogais)} vogais")
    print(f"Índices {indices_vogais}")

frase = input("Digite uma frase: ")
contar_vogais(frase)



6. from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    # Função para verificar se duas palavras são anagramas
    def sao_anagramas(palavra1, palavra2):
        return Counter(palavra1.lower()) == Counter(palavra2.lower())
    
    # Separar a frase em palavras
    palavras = frase.split()
    
    # Encontrar e retornar os anagramas da palavra objetivo
    anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo)]
    return anagramas

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

anagramas = encontrar_anagramas(frase, palavra_objetivo)
print(f"Anagramas: {anagramas}")



7. import random

def encrypt(nomes):
    # Gera uma chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)
    
    nomes_criptografados = []
    
    # Percorre cada nome na lista
    for nome in nomes:
        nome_criptografado = ""
        
        # Percorre cada caractere no nome e aplica a criptografia
        for char in nome:
            novo_char = chr(((ord(char) - 33 + chave) % 94) + 33)
            nome_criptografado += novo_char
        
        nomes_criptografados.append(nome_criptografado)
    
    return nomes_criptografados, chave

# Teste com a lista de nomes fornecida
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_aleatoria = encrypt(nomes)

# Exibe os nomes criptografados e a chave
print(f"Chave de criptografia: {chave_aleatoria}")
print(f"Nomes criptografados: {nomes_criptografados}")



8. def validar_cpf(cpf):
    # Remover pontos e traço do CPF
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verificar se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # Separar os 9 primeiros dígitos do CPF
    cpf_nove_digitos = cpf[:9]
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf_nove_digitos[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    primeiro_digito = 0 if resto < 2 else 11 - resto
    
    # Cálculo do segundo dígito verificador
    cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)
    soma = sum(int(cpf_dez_digitos[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    segundo_digito = 0 if resto < 2 else 11 - resto
    
    # Verificar se os dígitos calculados são iguais aos fornecidos
    if cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito):
        return "Válido"
    else:
        return "Inválido"

# Solicita o CPF do usuário
cpf = input("Digite um CPF no formato XXX.XXX.XXX-XX: ")
resultado = validar_cpf(cpf)
print(resultado)
