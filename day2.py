import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados de vendas
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
vendas = np.random.randint(100, 1000, len(meses))

# Criação do gráfico
plt.figure(figsize=(10,6))
plt.bar(meses, vendas, color='skyblue')
plt.xlabel('Meses')
plt.ylabel('Vendas (R$)')
plt.title('Vendas Mensais em 2023')
plt.xticks(rotation=45)
plt.show()
