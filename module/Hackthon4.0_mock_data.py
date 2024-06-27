import pandas as pd
import numpy as np

# 设置随机种子以保证结果可重复
np.random.seed(42)

# 生成模拟数据
num_samples = 10000

########
# 生成车辆使用数据

# 生成累积行驶时间
min_cumulative_driving_time = 500  # 最小累积行驶时间，例如1000小时
max_cumulative_driving_time = 3000  # 最大累积行驶时间，例如5000小时
cumulative_driving_time = np.random.randint(min_cumulative_driving_time, max_cumulative_driving_time, num_samples)

# 生成累积行驶里程 -- 平均速度 * 累积行驶时间
min_average_speed = 40  # 最小平均速度（公里/小时）
max_average_speed = 120  # 最大平均速度（公里/小时）
average_speeds = np.random.uniform(min_average_speed, max_average_speed, num_samples)
cumulative_mileage = average_speeds * cumulative_driving_time

# 引擎启动次数
average_mileage_per_start = 50  # 每次启动平均行驶100公里
base_engine_starts = cumulative_mileage / average_mileage_per_start # 根据累积行驶里程计算基础启动次数
# 假设噪声是正态分布的，且标准差为基础启动次数的10%
noise_starts = np.random.normal(0, base_engine_starts * 0.1, num_samples) # 添加随机噪声来模拟实际情况中的变化
engine_starts = np.round(base_engine_starts + noise_starts).astype(int) # 计算最终的引擎启动次数，并确保它们是整数
# 设置引擎启动次数的最小和最大值（可选）
engine_starts = np.clip(engine_starts, 100, 10000)

### 电池参数
# 假设电池循环次数与行驶里程成正比，并添加一些随机性
# 累积行驶
cycle_count = cumulative_mileage * 0.0001 + np.random.randint(-20, 50, num_samples)
cycle_count = np.clip(cycle_count, 0, None)  # 确保循环次数非负

# 车的型号 - 车的电池数
# 电压、电流、温度、内阻、外部环境温度
noise_amplitude = 0.5  # 增加了噪声幅度
base_voltage = 3.6
voltage = base_voltage - 0.001 * cycle_count + noise_amplitude * np.random.normal(size=num_samples)
voltage = np.clip(voltage, 3.0, 4.35)

current = 1.5 - 0.0005 * cycle_count + 0.5 * np.random.normal(size=num_samples)

temperature = 25 + 0.01 * cycle_count + 2 * np.random.normal(size=num_samples)
temperature = np.clip(temperature, 20, 60)

internal_resistance = 0.01 + 0.0001 * cycle_count + 0.0001 * np.random.normal(size=num_samples)
internal_resistance = np.clip(internal_resistance, 0.01, 0.15)

environment_temp = np.random.uniform(15, 35, num_samples)

# 还可以根据行驶时间和驾驶习惯来进一步调整电池容量损耗
# 例如，假设急加速和急刹车对电池损耗有额外影响
rapid_acceleration = np.random.randint(0, 100, num_samples)  # 急加速频率
sudden_braking = np.random.randint(0, 100, num_samples)  # 急刹车频率

# additional_wear = 0.01 * (rapid_acceleration + sudden_braking)  # 急加速和急刹车造成的额外损耗
# battery_capacity_history = 100 - (0.01 * cycle_count + additional_wear)
# battery_capacity_history = np.clip(battery_capacity_history, 0, 100)

# 假设电池损耗与驾驶习惯的关系
# 我们可以定义一个函数来计算电池损耗指数，这个指数越高，表示电池损耗越大
# def calculate_battery_wear_index(speed, rapid_acc, sudden_brake):
#     # 这里只是一个简单的线性模型，实际情况可能更复杂
#     wear_index = (speed / 100) + (rapid_acc / 100) + (sudden_brake / 100)
#     return wear_index
#
# # 计算电池损耗指数
# battery_wear_index = calculate_battery_wear_index(average_speeds, rapid_acceleration, sudden_braking)
#
# # 你可以使用这个电池损耗指数来进一步影响其他与电池相关的数据，比如电池寿命、电池容量等
# # 例如，可以根据电池损耗指数来调整电池寿命
# battery_life = 1000 - (battery_wear_index * 10)  # 假设电池初始寿命为1000小时，损耗指数越高，寿命越短
# battery_life = np.clip(battery_life, 100, 1000)  # 确保电池寿命在合理范围内


# 设定一个基于多个因素的损坏指标（虚构的，仅用于示例）
# 假设损坏与电池循环次数、内阻、急加速和急刹车频率正相关，与电池容量负相关
# 假设我们想要增加电池循环次数对damage_index的影响
cycle_count_coefficient = 2  # 原来的系数是0.01，现在增加到0.05

damage_index = (
        cycle_count_coefficient * cycle_count +  # 调整了系数的电池循环次数影响
        0.1 * internal_resistance +  # 内阻的影响
        (rapid_acceleration + 1.5) * 0.001 +  # 急加速频率的非线性影响
        (sudden_braking + 2) * 0.001 +  # 急刹车频率的非线性影响
        (10 - voltage) * 0.1 +  # 电压降低的影响
        np.abs(current - 1.5) * 0.1 +  # 电流偏离正常值的影响
        (temperature - 25) * 0.01  # 温度偏离最佳工作点的影响
)
# damage_index = np.clip(damage_index, 0, 1000)  # 确保损坏指标在合理范围内

# 创建DataFrame
data = pd.DataFrame({
    'voltage': voltage,
    'current': current,
    'temperature': temperature,
    'internal_resistance': internal_resistance,
    'environment_temp': environment_temp,
    'cycle_count': cycle_count,
    'average_speeds': average_speeds,
    'rapid_acceleration': rapid_acceleration,
    'sudden_braking': sudden_braking,
    'cumulative_mileage': cumulative_mileage,
    'cumulative_driving_time': cumulative_driving_time,
    'engine_starts': engine_starts,
    'damage_index': damage_index  # 这是我们的训练目标
})

# 保存为CSV文件
data.to_csv('vehicle_maintenance_data.csv', index=False)