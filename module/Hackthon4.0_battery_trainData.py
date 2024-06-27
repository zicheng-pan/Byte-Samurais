from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

# 读取生成的数据
data = pd.read_csv('battery_data.csv')

# 特征选择
features = ['电压', '电流', '温度', '内阻', '外部环境', '电池循环次数']
X = data[features]

# 假设我们有一个电池容量损耗的标签列'y'
# 模拟电池容量损耗随循环次数增加，并添加一些随机噪声
y = 0.02 * data['电池循环次数'] + 0.01 * np.random.normal(size=len(data))

# 数据分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 数据标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 模型训练
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 模型预测
y_pred = model.predict(X_test)

# 模型评估
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# 模型部署
# 可以将训练好的模型保存以供后续使用
import joblib

joblib.dump(model, 'battery_loss_model.pkl')
