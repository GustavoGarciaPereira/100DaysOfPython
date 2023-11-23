#com matplotlib


# import numpy as np
# import matplotlib.pyplot as plt

# # Parâmetros da simulação
# num_passos = 1000  # Número de passos no movimento
# num_particulas = 10  # Número de partículas a serem simuladas

# # Inicializando as posições das partículas
# posicoes = np.zeros((num_particulas, 2))  # Cada partícula tem uma posição (x, y)

# # Simulando o movimento
# for i in range(1, num_passos):
#     # Movimento aleatório: escolhe uma direção aleatória para cada partícula
#     passo = np.random.normal(0, 1, (num_particulas, 2))
#     posicoes += passo  # Atualiza a posição de cada partícula

#     # Plotando as trajetórias
#     plt.scatter(posicoes[:, 0], posicoes[:, 1], alpha=i/num_passos, c='blue')
#     plt.title("Movimento Browniano de Partículas")
#     plt.xlabel("Posição X")
#     plt.ylabel("Posição Y")
#     plt.pause(0.01)

# plt.show()



# import numpy as np
# import plotly.graph_objects as go
# import plotly.express as px

# # Parâmetros da simulação
# num_passos = 1000  # Número de passos no movimento
# num_particulas = 10  # Número de partículas a serem simuladas

# # Inicializando as posições das partículas
# posicoes = np.zeros((num_particulas, 2))  # Cada partícula tem uma posição (x, y)

# # Preparando o gráfico
# fig = go.Figure()

# # Simulando o movimento
# for i in range(1, num_passos):
#     # Movimento aleatório: escolhe uma direção aleatória para cada partícula
#     passo = np.random.normal(0, 1, (num_particulas, 2))
#     posicoes += passo  # Atualiza a posição de cada partícula

#     # Atualizando o gráfico
#     fig.add_trace(go.Scatter(x=posicoes[:, 0], y=posicoes[:, 1],
#                              mode='markers',
#                              marker=dict(size=10, opacity=i/num_passos),
#                              name=f'Passo {i}'))

# # Configurando o layout do gráfico
# fig.update_layout(title="Movimento Browniano de Partículas",
#                   xaxis_title="Posição X",
#                   yaxis_title="Posição Y",
#                   showlegend=False)

# # Mostrar o gráfico
# fig.show()
# import numpy as np
# from bokeh.plotting import figure, show, output_notebook
# from bokeh.models import ColumnDataSource
# from bokeh.io import push_notebook

# # Parâmetros da simulação
# num_passos = 1000  # Número de passos no movimento
# num_particulas = 10  # Número de partículas a serem simuladas

# # Inicializando as posições das partículas
# posicoes = np.zeros((num_particulas, 2))  # Cada partícula tem uma posição (x, y)

# # Preparando o gráfico
# output_notebook()  # Para exibir o gráfico no notebook
# source = ColumnDataSource(data=dict(x=posicoes[:, 0], y=posicoes[:, 1]))
# p = figure(title="Movimento Browniano de Partículas", x_axis_label='Posição X', y_axis_label='Posição Y')
# p.circle('x', 'y', source=source, size=8, color="navy", alpha=0.5)

# # Mostrando o gráfico
# handle = show(p, notebook_handle=True)

# # Simulando o movimento
# for i in range(1, num_passos):
#     # Movimento aleatório
#     passo = np.random.normal(0, 1, (num_particulas, 2))
#     posicoes += passo

#     # Atualizando o gráfico
#     source.data = dict(x=posicoes[:, 0], y=posicoes[:, 1])
#     push_notebook(handle=handle)
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Parâmetros da simulação
num_passos = 1000  # Número de passos no movimento
num_particulas = 10  # Número de partículas a serem simuladas

# Inicializando as posições das partículas
posicoes = np.zeros((num_particulas, num_passos, 2))  # Cada partícula tem uma posição (x, y) para cada passo

# Simulando o movimento
for i in range(1, num_passos):
    passo = np.random.normal(0, 1, (num_particulas, 2))
    posicoes[:, i, :] = posicoes[:, i - 1, :] + passo

# Preparando dados para Seaborn
dados_x = posicoes[:, :, 0].flatten()
dados_y = posicoes[:, :, 1].flatten()
hue = np.repeat(np.arange(num_particulas), num_passos)

# Criando o gráfico com Seaborn
sns.set(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=dados_x, y=dados_y, hue=hue, palette="colorblind", legend=False)
plt.title("Movimento Browniano de Partículas")
plt.xlabel("Posição X")
plt.ylabel("Posição Y")
plt.show()
