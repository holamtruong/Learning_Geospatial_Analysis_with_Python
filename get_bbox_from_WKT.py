from osgeo import ogr


def export2wkt():
    shape = ogr.Open("sample_data\polygon\polygon.shp")
    layer = shape.GetLayer()
    feature = layer.GetNextFeature()
    geom = feature.GetGeometryRef()
    wkt = geom.ExportToWkt()
    print(wkt)
    # return POLYGON ((-99.90467936217...))


def get_bounding_box():
    shape = ogr.Open("sample_data\polygon\polygon.shp")
    layer = shape.GetLayer()
    feature = layer.GetNextFeature()
    geom = feature.GetGeometryRef()
    wkt = geom.ExportToWkt()
    poly = ogr.CreateGeometryFromWkt(wkt)
    # GetEnvelope to get bbox
    bbox = poly.GetEnvelope()
    print(bbox)
    # return (-114.317157696392, -75.0103986030767, 23.2462726889969, 51.6981476867451)


if __name__ == "__main__":
    # export2wkt()
    get_bounding_box()
