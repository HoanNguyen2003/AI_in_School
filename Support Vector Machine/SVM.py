import numpy as np

def svm(X, y, w_init, lr=0.01, max_iter=1000, C=1.0):
    w = w_init.copy()
    d, n = X.shape

    for _ in range(max_iter):
        # Tính gradient
        grad_w = np.zeros_like(w)
        for i in range(n):
            xi = X[:, i].reshape(d, 1)
            yi = y[0, i]
            if yi * np.dot(w.T, xi) < 1:  # Điều kiện vi phạm margin
                grad_w += -yi * xi

        # Cập nhật trọng số
        w -= lr * (w + C * grad_w)  

    return w

if __name__ == '__main__':
    # Load dữ liệu
    data = np.genfromtxt('./Single Layer Perceptron Dataset 2.csv', delimiter=',', skip_header=1)
    data = data[~np.isnan(data).any(axis=1)]  

    X = data[:, 1:-1].T
    y = data[:, -1].reshape(1, -1).astype(int)

    Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)  # Thêm bias

    w_init = np.random.randn(Xbar.shape[0], 1)  # Khởi tạo trọng số

    w_svm = svm(Xbar, y, w_init)  

    print("Trọng số cuối cùng của SVM:", w_svm.T)
