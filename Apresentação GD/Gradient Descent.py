import numpy as np
import matplotlib.pyplot as plt

# 1. Gerar dados sintéticos
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 valores entre 0 e 2
y = 4 + 3 * X + np.random.randn(100, 1)  # Relação linear com ruído

# 2. Adicionar o termo de bias (x0 = 1)
X_b = np.c_[np.ones((100, 1)), X]

# 3. Hiperparâmetros
learning_rate = 0.1
n_iterations = 100

# 4. Inicializar parâmetros aleatoriamente
theta = np.random.randn(2, 1)

# 5. Armazenar histórico para visualização
theta_history = [theta]
loss_history = []

# 6. Algoritmo Gradient Descent
for iteration in range(n_iterations):
    # Calcular gradientes (usando TODOS os exemplos)
    gradients = 2/len(X_b) * X_b.T.dot(X_b.dot(theta) - y)
    
    # Atualizar parâmetros
    theta = theta - learning_rate * gradients
    
    # Armazenar histórico
    theta_history.append(theta.copy())
    loss = np.mean((X_b.dot(theta) - y) ** 2)
    loss_history.append(loss)

# 7. Visualização dos resultados
plt.figure(figsize=(16, 5))

# Gráfico 1: Evolução dos parâmetros
plt.subplot(1, 3, 1)
plt.plot([t[0] for t in theta_history], [t[1] for t in theta_history], 'b-',
         marker='o', markersize=4)
plt.xlabel(r'$\theta_0$ (bias)', fontsize=14)
plt.ylabel(r'$\theta_1$ (peso)', fontsize=14)
plt.title('Trajetória dos Parâmetros', fontsize=14)
plt.grid(True)

# Gráfico 2: Evolução do Loss
plt.subplot(1, 3, 2)
plt.plot(loss_history, 'r-')
plt.xlabel('Iteração', fontsize=14)
plt.ylabel('Loss (MSE)', fontsize=14)
plt.title('Evolução do Erro', fontsize=14)
plt.grid(True)

# Gráfico 3: Resultado final
plt.subplot(1, 3, 3)
plt.scatter(X, y, alpha=0.5)
plt.plot(X, X_b.dot(theta), 'r-', linewidth=2)
plt.xlabel('X', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title(f'Regressão Final\n y = {theta[1][0]:.2f}x + {theta[0][0]:.2f}', fontsize=14)
plt.grid(True)

plt.tight_layout()
plt.show()

# 8. Resultados numéricos
print("\nParâmetros finais:")
print(f"Intercepto (θ₀): {theta[0][0]:.4f}")
print(f"Inclinação (θ₁): {theta[1][0]:.4f}")
print(f"Erro final (MSE): {loss_history[-1]:.4f}")