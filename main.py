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
'''

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level']=="ERROR":
    print(f"{log['message']}")