import pandas as pd

# Tạo dữ liệu giống ảnh
data = {
    "Độ dài đài hoa": [5.1, 4.9, 4.7, 4.6, 5.0, 4.6, 5.4, 4.9, 5.0, 5.8, 6.3, 5.9, 6.5, 6.4, 4.9, 6.2, 6.7, 7.2],
    "Độ rộng đài hoa": [3.5, 3.4, 3.2, 3.1, 3.6, 3.4, 3.9, 3.1, 3.2, 2.7, 2.9, 3.2, 3.0, 2.9, 2.5, 2.9, 2.5, 3.6],
    "Độ dài cánh hoa": [1.4, 1.4, 1.3, 1.5, 1.4, 1.4, 1.7, 1.5, 1.4, 5.1, 5.6, 5.1, 5.8, 5.6, 4.5, 4.5, 5.8, 6.1],
    "Độ rộng cánh hoa": [0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.4, 0.1, 0.2, 1.9, 1.8, 2.1, 2.2, 2.2, 1.7, 1.5, 1.8, 2.5],
    "Tên loài": [
        "Iris setosa", "Iris setosa", "Iris setosa", "Iris setosa", "Iris setosa",
        "Iris setosa", "Iris setosa", "Iris setosa", "Iris setosa", "Iris virginica",
        "Iris virginica", "Iris virginica", "Iris virginica", "Iris virginica",
        "Iris virginica", "Iris virginica", "Iris virginica", "Iris virginica"
    ]
}

# Chuyển thành DataFrame
df = pd.DataFrame(data)

# Lưu thành file CSV
df.to_csv("iris_data.csv", index=False, encoding="utf-8-sig")

print("File iris_data.csv đã được tạo thành công!")
