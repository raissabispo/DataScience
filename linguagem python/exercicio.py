# dados
import random
import matplotlib.pyplot as plt
# grafico distribuição, estatisti
# ca de tendencia central

dados = [random.randint(0, 100) for _ in range(10)]
print("Dados: ", dados)

# Estatisticas

media = sum(dados) / len(dados)
dados_sorted = sorted(dados)
mediana = (dados_sorted[4] + dados_sorted[5]) / 2
desvio = (sum((x - media) ** 2 for x in dados) /len(dados)) ** 0.5

print(f"Média: {media:.2f}, mediana: {mediana}, desvio: {desvio:.2f}")

# Histograma




plt.hist(dados, bins=5,edgecolor="black")
plt.title("Distribuição dos Dados")
plt.show()