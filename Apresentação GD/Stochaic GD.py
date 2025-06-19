import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Gerar dados (100 amostras)
np.random.seed(42)
X = np.random.rand(100, 1)  # Features (0 a 1)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)  # Rótulos (y = 2x + 1 + ruído)

# Converter para tensores do PyTorch
X_tensor = torch.from_numpy(X).float()
y_tensor = torch.from_numpy(y).float()

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)  # 1 entrada, 1 saída (y = wx + b)
    
    def forward(self, x):
        return self.linear(x)

model = LinearRegression()

criterion = nn.MSELoss()  # Erro quadrático médio
optimizer = optim.SGD(model.parameters(), lr=0.1)  # SGD com taxa de aprendizado = 0.1

epochs = 50
losses = []

for epoch in range(epochs):
    # Zerar os gradientes
    optimizer.zero_grad()
    
    # Forward pass (predição)
    outputs = model(X_tensor)
    
    # Calcular perda
    loss = criterion(outputs, y_tensor)
    losses.append(loss.item())
    
    # Backward pass (gradiente)
    loss.backward()
    
    # Atualizar parâmetros (SGD)
    optimizer.step()
    
    # Print a cada 10 épocas
    if (epoch+1) % 10 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')

# Plotar dados e linha ajustada
plt.scatter(X, y, label='Dados reais')
plt.plot(X, model(X_tensor).detach().numpy(), 'r-', label='Modelo treinado')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# Plotar perda ao longo do treinamento
plt.plot(losses)
plt.xlabel('Época')
plt.ylabel('Loss (MSE)')
plt.title('Convergência do SGD')
plt.show()