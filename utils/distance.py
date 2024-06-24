from math import radians, cos, sin, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees).

    Args:
        lat1, lon1: 第一点的纬度和经度
        lat2, lon2: 第二点的纬度和经度

    Returns:
        距离，单位为公里
    """
    # 将经纬度转换为弧度
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # 经度差
    dlon = lon2 - lon1

    # 纬度差
    dlat = lat2 - lat1

    # Haversine公式
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # 地球半径，单位为公里
    r = 6371.0

    # 计算距离
    return c * r


# 示例使用
# point1 = (39.9042, 116.4074)  # 北京的经纬度
# point2 = (31.2304, 121.4737)  # 上海的经纬度
#
# distance = haversine(point1[0], point1[1], point2[0], point2[1])
# print(f"两点之间的距离是: {distance:.2f} 公里")
