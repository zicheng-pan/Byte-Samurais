import pandas as pd
import numpy as np

# 设置随机种子以保证结果可重复
np.random.seed(42)

# 生成模拟数据
num_samples = 1000
cycle_count = np.random.randint(0, 1000, num_samples)  # 电池循环次数范围 0 - 1000

# 电压随着循环次数增加而略微下降，添加一些随机噪声
voltage = 4.2 - 0.001 * cycle_count + 0.02 * np.random.normal(size=num_samples)  # 电压范围 3.0V - 4.2V

# 电流随着循环次数增加而略微变化，添加一些随机噪声
current = 1.5 - 0.0005 * cycle_count + 0.5 * np.random.normal(size=num_samples)  # 电流范围 -2.0A - 2.0A

# 温度随着循环次数增加而略微上升，添加一些随机噪声
temperature = 25 + 0.01 * cycle_count + 2 * np.random.normal(size=num_samples)  # 温度范围 20°C - 60°C

# 内阻随着循环次数增加而增加，添加一些随机噪声
internal_resistance = 0.01 + 0.0001 * cycle_count + 0.0001 * np.random.normal(size=num_samples)  # 内阻范围 0.01Ω - 0.15Ω

# 外部环境温度与电池循环次数无关，随机生成
environment_temp = np.random.uniform(15, 35, num_samples)  # 外部环境温度范围 15°C - 35°C

# 创建DataFrame
data = pd.DataFrame({
    '电压': voltage,
    '电流': current,
    '温度': temperature,
    '内阻': internal_resistance,
    '外部环境': environment_temp,
    '电池循环次数': cycle_count,
})

# 保存为CSV文件
data.to_csv('battery_data.csv', index=False)
#
# # 打印前几行数据查看
# print(data.head())
#
# import pandas as pd
# import numpy as np
#
# # 设置随机种子以保证结果可重复
# np.random.seed(42)
#
# # 生成模拟数据
# num_samples = 1000
# cycle_count = np.random.randint(0, 1000, num_samples)  # 电池循环次数范围 0 - 1000
#
# # 模拟电压、电流、温度、内阻和外部环境温度与电池循环次数之间的关系
# voltage = 4.2 - 0.001 * cycle_count + 0.02 * np.random.normal(size=num_samples)  # 电压范围 3.0V - 4.2V
# current = 1.5 - 0.0005 * cycle_count + 0.5 * np.random.normal(size=num_samples)  # 电流范围 -2.0A - 2.0A
# temperature = 25 + 0.01 * cycle_count + 2 * np.random.normal(size=num_samples)  # 温度范围 20°C - 60°C
# internal_resistance = 0.01 + 0.0001 * cycle_count + 0.0001 * np.random.normal(size=num_samples)  # 内阻范围 0.01Ω - 0.15Ω
# environment_temp = np.random.uniform(15, 35, num_samples)  # 外部环境温度范围 15°C - 35°C
#
# # 创建DataFrame
# data = pd.DataFrame({
#     '电压': voltage,
#     '电流': current,
#     '温度': temperature,
#     '内阻': internal_resistance,
#     '外部环境': environment_temp,
#     '电池循环次数': cycle_count,
# })
#
# # 打印前几行数据查看
# print(data.head())
#
# # 保存为CSV文件
# data.to_csv('data/battery_data.csv', index=False)
