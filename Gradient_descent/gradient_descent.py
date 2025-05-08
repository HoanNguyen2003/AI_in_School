import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

class LinearRegressionGD:
    def __init__(self, data_path, learning_rate=0.01):
        data = genfromtxt(data_path, delimiter=',', skip_header=1)
        self.X = data[:, 0:3]
        self.y = data[:, 3:4]
        self.N = data.shape[0]
        self.learning_rate = learning_rate
        self._normalize_data()
        self.X_b = np.c_[np.ones((self.N, 1)), self.X]

    def _normalize_data(self):
        self.X = (self.X - np.mean(self.X, axis=0)) / (np.max(self.X, axis=0) - np.min(self.X, axis=0))

    def batch_gradient_descent(self, epochs=100):
        thetas = np.random.randn(4, 1)
        losses = []
        
        for _ in range(epochs):
            y_hat = self.X_b.dot(thetas)
            loss = (y_hat - self.y) ** 2
            gradients = self.X_b.T.dot(2 * (y_hat - self.y) / self.N)
            thetas -= self.learning_rate * gradients
            losses.append(np.sum(loss) / self.N)
        
        return thetas, losses

    def mini_batch_gradient_descent(self, epochs=50, batch_size=30):
        thetas = np.random.randn(4, 1)
        losses = []
        
        for _ in range(epochs):
            shuffled_indices = np.random.permutation(self.N)
            X_shuffled, y_shuffled = self.X_b[shuffled_indices], self.y[shuffled_indices]
            
            for i in range(0, self.N, batch_size):
                xi, yi = X_shuffled[i:i + batch_size], y_shuffled[i:i + batch_size]
                y_hat = xi.dot(thetas)
                loss = (y_hat - yi) ** 2
                gradients = xi.T.dot(2 * (y_hat - yi) / batch_size)
                thetas -= self.learning_rate * gradients
                losses.append(np.sum(loss) / batch_size)
        
        return thetas, losses

    def plot_loss(self, losses, num_samples=100):
        plt.plot(range(num_samples), losses[:num_samples], color='r')
        plt.show()

model = LinearRegressionGD('./csv/advertising.csv')

bgd_thetas, bgd_losses = model.batch_gradient_descent()
model.plot_loss(bgd_losses)
print("Theta N=N:\n", bgd_thetas)

mbgd_thetas, mbgd_losses = model.mini_batch_gradient_descent()
model.plot_loss(mbgd_losses, num_samples=200)
print("Theta N=m=30:\n", mbgd_thetas)

sgd_thetas, sgd_losses = model.mini_batch_gradient_descent(epochs=50, batch_size=1)
model.plot_loss(sgd_losses, num_samples=200)
print("Theta N=1:\n", sgd_thetas)
