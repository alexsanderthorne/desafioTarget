import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

# Encontrando o menor e o maior valor de faturamento
menor_valor = float('inf')
maior_valor = float('-inf')
for d in dados:
    if d['valor'] > 0:
        if d['valor'] < menor_valor:
            menor_valor = d['valor']
        if d['valor'] > maior_valor:
            maior_valor = d['valor']

# Calculando a média de faturamento
soma = 0
contagem = 0
for d in dados:
    if d['valor'] > 0:
        soma += d['valor']
        contagem += 1
media = soma / contagem

# Contando o número de dias com faturamento acima da média
acima_da_media = 0
for d in dados:
    if d['valor'] > media:
        acima_da_media += 1

# Imprimindo os resultados
print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Dias com faturamento acima da média:", acima_da_media)
