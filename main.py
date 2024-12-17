'''
Exercício 1: Verificação de Qualidade de Dados
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para 
quantidade e preço. 
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

https://www.digitalocean.com/community/tutorials/python-valueerror-exception-handling-examples
https://www.pythonforbeginners.com/basics/typeerror-in-python


try:
    qnt = int(input("Insira a quantidade"))
    preco = int(input("Insira o preço "))

    if( qnt and preco >= 0):
        print("Dados Validos")
    else:
        print("Dados Inválidos")

except ValueError:
    print("Valor digitado não é numerico")
    
'''
'''
Exercício 2: Classificação de Dados de Sensor
Imagine que você está trabalhando com dados de sensores IoT.
 Os dados incluem medições de temperatura. 
 Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'


try:
    temp = float(input("Digite a temperatura: "))

    if (temp < 18):
        print("Temperatura Baixa")
    elif (temp >=18 and temp <= 26):
        print("Temperatura Normal")
    else:
        print("Temperatura Alta")

except ValueError:
    print("Valor digitado não é numerico")
except TypeError:
    print("Dado Invalido")

'''

'''

Exercício 3: Filtragem de Logs por Severidade
Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'.
Dado um registro de log em formato de dicionário como 
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, 
escreva um programa que imprima a mensagem se a severidade for 'ERROR'.


log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level']=="ERROR":
    print(f"{log['message']}")

'''

'''
Exercício 4: Validação de Dados de Entrada
Antes de processar os dados de usuários em um sistema de recomendação, 
você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. 
Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

'''

'''
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade:"))
email = input("Digite seu email: ")
 
if (idade in range(18,66) and "@" in email and "." in email):
    print("Valido")
else:
     print("invalido")

'''
'''
Exercício 5: Detecção de Anomalias em Dados de Transações
Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. 
Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial 
(antes das 9h ou depois das 18h). 
Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

transacao = {'valor': 18000, 'hora': 14}

if (transacao["valor"] >= 10000 or 9<=transacao["hora"]>18):
     print("Operação Suspeita")
else:
     print("Operação valida")
'''
