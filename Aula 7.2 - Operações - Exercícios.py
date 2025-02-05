1.  def data_por_extenso(data_nascimento):
    # Lista com os meses por extenso
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Dividindo a data em dia, mês e ano
    dia, mes, ano = data_nascimento.split('/')
    
    # Convertendo o mês para o nome correspondente (meses começa do índice 0, então subtraímos 1)
    mes_extenso = meses[int(mes) - 1]
    
    # Retornando a data formatada
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."

# Solicitando a data de nascimento do usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Imprimindo a data com o mês por extenso
print(data_por_extenso(data_nascimento))




2.  def substituir_vogais(frase):
    # Lista com as vogais
    vogais = "aeiouAEIOU"
    
    # Substituindo as vogais por '*'
    frase_modificada = ''.join('*' if letra in vogais else letra for letra in frase)
    
    return frase_modificada

# Solicitando ao usuário para inserir uma frase
frase = input("Digite uma frase: ")

# Imprimindo a frase modificada
print("Frase modificada:", substituir_vogais(frase))




3. import string

def eh_palindromo(frase):
    # Removendo espaços, pontuações e convertendo para letras minúsculas
    frase_limpa = ''.join(letra.lower() for letra in frase if letra.isalnum())
    
    # Verificando se a frase limpa é igual à sua reversa
    return frase_limpa == frase_limpa[::-1]

# Loop principal para solicitar frases ao usuário
while True:
    # Solicitando ao usuário para inserir uma frase
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    # Verificando se o usuário deseja encerrar o programa
    if frase.lower() == "fim":
        break
    
    # Verificando se a frase é um palíndromo
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')
``




4. import re

def validador_senha(senha):
    # Verificar se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verificar se a senha contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False
    
    # Verificar se a senha contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False
    
    # Verificar se a senha contém pelo menos um número
    if not re.search(r'[0-9]', senha):
        return False
    
    # Verificar se a senha contém pelo menos um caractere especial
    if not re.search(r'[@#$]', senha):
        return False
    
    # Se passar por todos os testes, retorna True
    return True

# Exemplos de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False




5.  import random

def embaralhar_palavras(frase):
    # Função auxiliar para embaralhar as letras internas de uma palavra
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])  # Pegando as letras internas
        random.shuffle(meio)        # Embaralhando as letras internas
        return palavra[0] + ''.join(meio) + palavra[-1]

    # Dividir a frase em palavras e aplicar a função em cada uma
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    
    # Juntar as palavras embaralhadas em uma frase
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
