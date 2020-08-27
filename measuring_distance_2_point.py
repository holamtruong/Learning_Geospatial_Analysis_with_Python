import math


def cal_distance():
    # Ben Tre (x1, y1)
    x1 = 106.354266
    y1 = 10.249546
    # HCM (x2, y2)
    x2 = 106.701141
    y2 = 10.776503

    x_dist = math.radians(x1 - x2)
    y_dist = math.radians(y1 - y2)
    dist_sq = x_dist ** 2 + y_dist ** 2
    dist_rad = math.sqrt(dist_sq)
    dist_xy = dist_rad * 6371251.46
    print(dist_xy)
    # 70153.10431163161 m


if __name__ == "__main__":
    cal_distance()
