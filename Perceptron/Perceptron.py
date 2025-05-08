import numpy as np

def pred(w, x):
    return np.sign(np.dot(w.T, x))

def perceptron_loss(X, y, w_init, alpha=1, max_inter=1000):
    w = w_init
    d = X.shape[0]
    iter_count = 0
    
    while iter_count < max_inter:
        converged = []
        
        for i in range(X.shape[1]):
            xi = X[:, i].reshape(d, 1)
            yi = y[0, i]
            
            if pred(w, xi)[0] != yi:
                converged.append(i)
        
        if not converged:
            break  
        
        # Gradient Descent cập nhật trọng số dựa trên tổng khoảng cách
        grad = np.sum([y[0, i] * X[:, i].reshape(d, 1) for i in converged], axis=0)
        w = w + alpha * grad
        
        iter_count += 1
    
    return w

if __name__ == '__main__':
    data = np.genfromtxt('./Single Layer Perceptron Dataset 2.csv', delimiter=',', skip_header=1)
    data = data[~np.isnan(data).any(axis=1)]
    
    X = data[:, 1:-1].T
    y = data[:, -1].reshape(1, -1).astype(int)
    
    Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)
    
    w_init = np.random.randn(Xbar.shape[0], 1)
    
    w_final = perceptron_loss(Xbar, y, w_init, alpha=0.1)
    
    print("Trọng số cuối cùng:", w_final.T)