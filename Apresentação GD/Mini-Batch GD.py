import numpy as np
import matplotlib.pyplot as plt
from IPython import display  # Para atualizar o gráfico dinamicamente (opcional)

# 1. Gerar dados sintéticos
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 2. Hiperparâmetros
learning_rate = 0.1
n_epochs = 100
batch_size = 16
n_samples = len(X)

# 3. Inicializar parâmetros
theta = np.random.randn(2, 1)

# 4. Adicionar coluna de 1s para o bias
X_b = np.c_[np.ones((n_samples, 1)), X]

# 5. Configurar gráficos
plt.figure(figsize=(12, 4))

# Lista para armazenar o histórico do loss
loss_history = []

# 6. Mini-Batch Gradient Descent
for epoch in range(n_epochs):
    # Embaralhar os dados
    shuffled_indices = np.random.permutation(n_samples)
    X_shuffled = X_b[shuffled_indices]
    y_shuffled = y[shuffled_indices]
    
    # Iterar sobre mini-batches
    for i in range(0, n_samples, batch_size):
        X_batch = X_shuffled[i:i+batch_size]
        y_batch = y_shuffled[i:i+batch_size]
        
        # Calcular gradiente e atualizar theta
        gradients = (2 / batch_size) * X_batch.T.dot(X_batch.dot(theta) - y_batch)
        theta -= learning_rate * gradients
    
    # Calcular e armazenar o loss após cada época
    loss = np.mean((X_b.dot(theta) - y) ** 2)
    loss_history.append(loss)
    
    # Plotar gráficos a cada 5 épocas (para não ficar muito lento)
    if epoch % 1 == 0:
        plt.clf()  # Limpar o gráfico anterior
        
        # Gráfico 1: Dados e Regressão
        plt.subplot(1, 2, 1)
        plt.scatter(X, y, alpha=0.5, label='Dados reais')
        plt.plot(X, X_b.dot(theta), 'r-', label='Regressão')
        plt.title(f'Época {epoch}\n y = {theta[1][0]:.2f}x + {theta[0][0]:.2f}')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        
        # Gráfico 2: Evolução do Loss
        plt.subplot(1, 2, 2)
        plt.plot(loss_history, 'b-')
        plt.title('Loss (MSE) por Época')
        plt.xlabel('Época')
        plt.ylabel('Loss')
        plt.grid(True)
        
        display.clear_output(wait=True)  # Atualizar dinamicamente (Jupyter)
        plt.pause(0.1)  # Pausa para visualização (opcional)

plt.show()

# 7. Resultados Finais
print("\nParâmetros finais:")
print(f"Intercepto (theta0): {theta[0][0]:.4f}")
print(f"Inclinação (theta1): {theta[1][0]:.4f}")