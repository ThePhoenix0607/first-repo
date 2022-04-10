# Comentário no python (comentar é importante)

# O que são variáveis?
# Variáveis são espaços na memória que você avisa que vai usar
# como por exemplo um campo "nome" que guardará o nome do usuário.

nome = "Jorge"
# As aspas são para explicar que isso é um texto, ou melhor dizendo, String

# Existem tipos de dados na programação
# Int -> 10
# String -> Olá, sou o Jorge e tenho 18 anos.
# Float -> 1.73
# Boolean -> True

# Existem comandos específicos, alguns podem ser usados para mostrar dados, e até mesmo 
# realizar alguma ação com eles, mas antes, vamos ver algumas estruturas

# Estruturas de decisão
if nome == "João":
    print("olá" + nome)
elif nome == "Jorge":
    print("Olá" + nome)
else:
    print("Qual seu nome?")

# Estruturas de repetição
for i in range(10):
    print(i)

# # O que são funções?
# # Blocos de código

# def perguntarIdade():
#     print("Olá mundo")

# # Uma função só é executada, se chamarmos ela
# # desse jeito -> perguntarIdade()

# # Uma função pode retornar um valor para utilizarmos, assim deixando o código mais organizado
# # e mais independência no código

# def perguntarIdade():
#     idade = int(input("Qual sua idade?\n"))
#     return idade

# print(perguntarIdade())
# # Aqui estamos printando o retorno da def perguntarIdade()

# # Podemos agora falar que uma função PRECISA de valores para ser chamada
# def maioridade(idade):
#     if idade >= 18:
#         print("Pode ir beber")
#     else:
#         print("Você é de menor")


# idade =  perguntarIdade()
# maioridade(idade)