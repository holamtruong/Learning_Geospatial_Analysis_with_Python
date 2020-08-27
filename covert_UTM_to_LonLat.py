import utm


def covert_UTM2lonlat():
    y = 648319.851650864
    x = 1133315.3261852388
    zone = 48
    band = 'P'
    print(utm.to_latlon(y, x, zone, band))
    # (10.249546000733893, 106.35426599999911)  -- Ben Tre


if __name__ == "__main__":
    covert_UTM2lonlat()
