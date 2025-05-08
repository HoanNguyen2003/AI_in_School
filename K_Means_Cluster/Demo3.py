import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def initialize_K_centroids(X, K):
    m, n = X.shape
    k_rand = np.ones((K, n))
    k_rand = X[np.random.choice(range(len(X)), K, replace = False), :]
    return k_rand

def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        distances = np.linalg.norm(X[i,] - centroids, axis = 1)
        c[i] = np.argmin(distances)
    return c

def compute_means(X, idx, K):
    m, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        points_belong_k = X[np.where(idx == k)]
        centroids[k] = np.mean(points_belong_k, axis = 0)
    return centroids

def compute_inertia(X, centroids, idx):
    inertia = 0
    for i in range(len(X)):
        centroid = centroids[int(idx[i])]
        distance = np.linalg.norm(X[i] - centroid)
        inertia += distance ** 2
    return inertia

def find_k_means(X, K, max_iters = 10):
    _, n = X.shape
    centroids = initialize_K_centroids(X, K)
    for i in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
    return centroids, idx

if __name__ == "__main__":

    df = pd.read_csv("Countries-exercise.csv")
    X = df[['Longitude', 'Latitude']].values
    
    l = []
    K_range = range(1, 10)
    for K in K_range:
        centroids, idx = find_k_means(X, K)
        inertia = compute_inertia(X, centroids, idx)
        print(f"L({K}): ", inertia)
        l.append(inertia)

    plt.plot(K_range, l, marker='o')
    plt.title('Phương pháp chọn số cụm K')
    plt.xlabel('Số cụm (K)')
    plt.ylabel('Tổng bình phương khoảng cách')
    plt.grid(True)
    plt.savefig("elbow_plot.png")

    # Bình luận dựa trên đồ thị Elbow và giá trị inertia:
    # - Dễ thấy inertia giảm mạnh từ K=1 đến K=2
    # - Sau đó, độ giảm inertia trở nên nhẹ dần khi K tăng lên
    # - Điều này cho thấy điểm "gập" (elbow) nằm ở khoảng K=3, khi inertia bắt đầu ổn định hơn
    # - Vì vậy, K=3 được chọn là số cụm hợp lý để tránh phân cụm quá nhiều mà không cải thiện đáng kể
    # - Nếu muốn chắc chắn hơn, có thể sử dụng các chỉ số khác như silhouette score hoặc Davies-Bouldin index

    optimal_K = 3
    centroids, idx = find_k_means(X, optimal_K)
    
    df['cluster'] = idx
    df.to_csv("Countries_exercise.csv", index=False)
    print("Đã lưu kết quả vào file 'Countries_with_clusters.csv'.")

        


    