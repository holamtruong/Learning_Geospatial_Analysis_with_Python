from math import atan2, cos, sin, degrees


def cal_direction():
    # Ben Tre
    lon1 = 106.354266
    lat1 = 10.249546
    # HCM
    lon2 = 106.701141
    lat2 = 10.776503
    angle = atan2(cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(lon2 - lon1), sin(lon2 - lon1) * cos(lat2))
    bearing = (degrees(angle) + 360) % 360
    print(bearing)
    # 98


if __name__ == "__main__":
    cal_direction()
