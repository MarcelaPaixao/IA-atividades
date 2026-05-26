import matplotlib.pyplot as plt
import numpy as np

# 1. Definir o intervalo de x
# Usamos 1000 pontos para capturar bem todas as oscilações rápidas da função
x = np.linspace(-2, 2, 1000)

# 2. Definir a equação desejada
y = x * np.sin(10 * np.pi * x) + 1

# 3. Criar o gráfico
plt.plot(x, y)

# 4. Customização do gráfico
plt.title('Gráfico da Função Osciante')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.grid(True)

plt.savefig('tst.png')