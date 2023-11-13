import numpy as np

import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
import pandas as pd

# Carregar dados do arquivo CSV
df = pd.read_csv('statusinvest-busca-avancada.csv', delimiter=';', decimal=',')
print(df.head())
df.hist()
print(df.describe())

# Aqui você precisará adaptar 'caminho_para_seu_arquivo.csv' para o caminho do seu arquivo CSV real

# drop nan of df['ROE']
df = df.dropna(subset=['ROE'])

# replace ',' to '' of df['ROE']
df['ROE'] = df['ROE'].str.replace(',', '').replace('.', '')

df['ROE'] = pd.to_numeric(df['ROE'], errors='coerce')
retorno_esperado = df['ROE'].mean() / 100  # Convertendo de porcentagem para decimal

# Aqui você precisaria calcular a volatilidade histórica dos preços das ações (PRECO)
# A volatilidade poderia ser estimada por exemplo como o desvio padrão dos retornos logarítmicos dos preços

precos = df['PRECO']
retornos_log = np.log(precos / precos.shift(1))
volatilidade = retornos_log.std()  # Volatilidade histórica

# Parâmetros iniciais
preco_inicial = 100  # Preço inicial da ação
# retorno_esperado = 0.07  # Retorno esperado anual
# volatilidade = 0.2  # Volatilidade anual
horizonte_temporal = 1  # Horizonte temporal em anos
intervalos = 252  # Número de intervalos de negociação por ano
simulacoes = 1000  # Número de simulações

# Geração dos choques aleatórios e cálculo dos preços diários
np.random.seed(0)  # Para resultados consistentes
choques = np.random.normal(0, 1, (intervalos, simulacoes))
retorno_diario = (retorno_esperado / intervalos) + (volatilidade * choques * (1 / np.sqrt(intervalos)))
precos_simulados = preco_inicial * np.cumprod(1 + retorno_diario, axis=0)

# Análise dos resultados
preco_final_medio = np.mean(precos_simulados[-1])
mediana_final = np.median(precos_simulados[-1])
var_95 = np.percentile(precos_simulados[-1], 5)

print(f"Preço final médio: {preco_final_medio}")
print(f"Mediana do preço final: {mediana_final}")
print(f"Valor em Risco (VaR) 95%: {preco_inicial - var_95}")

# Plotagem dos resultados (opcional, requer matplotlib)
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(precos_simulados)
plt.title('Simulação de Monte Carlo para Previsão de Preço de Ação')
plt.xlabel('Dias')
plt.ylabel('Preço da Ação')
plt.show()
