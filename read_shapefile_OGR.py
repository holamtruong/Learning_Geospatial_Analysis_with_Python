import ogr


def read_and_print_shp():
    shp = ogr.Open("sample_data\point\point.shp")
    layer = shp.GetLayer()
    for feature in layer:
        geometry = feature.GetGeometryRef()
        # print(geometry)
        x = geometry.GetX()
        y = geometry.GetY()
        print(x, y, feature.GetField("FIRST_FLD"))

        # 1.0 1.0 First
        # 3.0 1.0 Second
        # 4.0 3.0 Third
        # 2.0 2.0 Fourth
        # 0.0 0.0 Appended


if __name__ == "__main__":
    read_and_print_shp()
