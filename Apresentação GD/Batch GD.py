import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# 1. Gerar dados sintéticos (y = 2x + 1 + ruído)
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 valores entre 0 e 2
y = 1 + 2 * X + np.random.randn(100, 1)  # y = 1 + 2x + ruído

# 2. Adicionar o termo de viés (x0 = 1)
X_b = np.c_[np.ones((100, 1)), X]  # Matriz X com coluna de 1s (bias)

# 3. Hiperparâmetros
learning_rate = 0.1
n_epochs = 10000  # Número de épocas
m = len(X)       # Número de amostras

# 4. Inicialização dos parâmetros (theta0 e theta1)
theta = np.random.randn(2, 1)  # Valores aleatórios

# 5. Armazenar o histórico do custo (para plotagem)
cost_history = []

# 6. Batch Gradient Descent
for epoch in range(n_epochs):
    # Calcular gradiente (usando TODOS os exemplos)
    gradients = (2/m) * X_b.T.dot(X_b.dot(theta) - y)  # Gradiente do MSE
    
    # Atualizar parâmetros
    theta = theta - learning_rate * gradients
    
    # Calcular e armazenar o erro (MSE)
    cost = (1/m) * np.sum((X_b.dot(theta) - y) ** 2)
    cost_history.append(cost)
# 7. Resultados finais
print("Parâmetros finais (theta0 e theta1):", theta.flatten())

# 8. Plotar a convergência
plt.plot(range(n_epochs), cost_history)
plt.xlabel("Época")
plt.ylabel("Erro (MSE)")
plt.title("Convergência do Batch Gradient Descent")
plt.show()




