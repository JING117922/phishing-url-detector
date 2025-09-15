import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 正确设置 CSV 路径
csv_path = os.path.join("data", "dataset.csv")

# 加载 CSV 文件（尝试处理乱码）
try:
    data = pd.read_csv(csv_path, encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv(csv_path, encoding='latin1')  # 有些老CSV会用这个编码

# 显示前几行检查内容
print("前5行数据：")
print(data.head())

# 如果列名不对，打印所有列名确认
print("\n所有列名：", data.columns.tolist())

# 尝试从列中提取 URL 和 标签（可能列名不同）
if 'url' in data.columns and 'label' in data.columns:
    X = data['url']
    y = data['label']
else:
    raise ValueError("CSV文件中找不到 'url' 和 'label' 列，请检查列名是否正确。")

# 特征提取
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# 建模训练
model = LogisticRegression()
model.fit(X_train, y_train)

# 预测与评估
y_pred = model.predict(X_test)
print("\n分类报告：")
print(classification_report(y_test, y_pred))
