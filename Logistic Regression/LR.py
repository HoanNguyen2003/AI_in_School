import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

def sigmoid(s):
    return 1 / (1 + np.exp(-s))

def logistic_sigmoid_regression(X, y, w_init, eta, epsilon=1e-10, M=10000):
    w = [w_init]
    N, d = X.shape[1], X.shape[0]
    count, check_w_after = 0, 20
    
    while count < M:
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + eta * (yi - zi) * xi
            count += 1
            if count % check_w_after == 0 and np.linalg.norm(w_new - w[-check_w_after]) < epsilon:
                return w
            w.append(w_new)
    return w

def plot_decision_boundary(w, X, y, X_test=None, y_test=None):
    xx = np.linspace(min(X[1]) - 1, max(X[1]) + 1, 100)
    w0, w1 = w[-1][0][0], w[-1][1][0]
    yy = sigmoid(w0 + w1 * xx)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(X[1, np.where(y == 0)], np.zeros_like(X[1, np.where(y == 0)]), color='red', label='Train - Iris setosa (0)')
    plt.scatter(X[1, np.where(y == 1)], np.ones_like(X[1, np.where(y == 1)]), color='blue', label='Train - Not Iris setosa (1)')
    plt.plot(xx, yy, 'g-', linewidth=2, label='Decision Boundary')
    plt.axhline(0.5, color='gray', linestyle='dashed')
    plt.xlabel('Feature')
    plt.ylabel('Predicted Probability')
    plt.legend()
    plt.title('Train Data - Logistic Regression Decision Boundary')
    plt.show()
    
    if X_test is not None and y_test is not None:
        plt.figure(figsize=(8, 6))
        plt.scatter(X_test[1, np.where(y_test == 0)], np.zeros_like(X_test[1, np.where(y_test == 0)]), color='orange', marker='x', label='Test - Iris setosa (0)')
        plt.scatter(X_test[1, np.where(y_test == 1)], np.ones_like(X_test[1, np.where(y_test == 1)]), color='green', marker='x', label='Test - Not Iris setosa (1)')
        plt.plot(xx, yy, 'g-', linewidth=2, label='Decision Boundary')
        plt.axhline(0.5, color='gray', linestyle='dashed')
        plt.xlabel('Feature')
        plt.ylabel('Predicted Probability')
        plt.legend()
        plt.title('Test Data - Logistic Regression Decision Boundary')
        plt.show()

if __name__ == '__main__':

    #Training
    data = pd.read_csv('.\\train.csv')
    X, y = data.iloc[:, :-1].values.T, (data.iloc[:, -1] == 'Iris setosa').astype(int).values
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X.T).T
    Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)
    
    w_init = np.random.randn(Xbar.shape[0], 1)
    w = logistic_sigmoid_regression(Xbar, y, w_init, eta=0.05)
    
    y_pred = (sigmoid(np.dot(w[-1].T, Xbar)).flatten() >= 0.5).astype(int)
    
    #Testing
    X_test = pd.read_csv('.\\features.csv').values.T
    y_test = (pd.read_csv('.\\labels.csv').values.flatten() == 'Iris setosa').astype(int)
    X_test = scaler.transform(X_test.T).T
    Xbar_test = np.concatenate((np.ones((1, X_test.shape[1])), X_test), axis=0)
    
    y_test_pred = (sigmoid(np.dot(w[-1].T, Xbar_test)).flatten() >= 0.5).astype(int)
    
    plot_decision_boundary(w, Xbar, y, Xbar_test, y_test)
