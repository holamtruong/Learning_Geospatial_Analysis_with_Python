import ogr


def check_CRS():
    shp = ogr.Open("sample_data\polygon\polygon.shp")
    layer = shp.GetLayer()
    geometry = layer.GetSpatialRef()
    print(geometry)


if __name__ == "__main__":
    check_CRS()
