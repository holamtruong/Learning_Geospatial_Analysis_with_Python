import utm


def covert_lonlat2UTM():
    y = 106.354266
    x = 10.249546
    rs = utm.from_latlon(x, y)
    print(rs)
    # (648319.851650864, 1133315.3261852388, 48, 'P')  -- Ben Tre


if __name__ == "__main__":
    covert_lonlat2UTM()
