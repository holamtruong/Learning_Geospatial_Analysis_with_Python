import geojson

location_A = [-92, 37]


def xy_to_geojson():
    p = geojson.Point(location_A)
    print(p)
    # {"coordinates": [-92, 37], "type": "Point"}


def geojson_to_point():
    p = geojson.Point(location_A)
    geojs = geojson.dumps(p, indent=4)
    print(geojs)

    #
    # {
    #     "type": "Point",
    #     "coordinates": [
    #         -92,
    #         37
    #     ]
    # }


if __name__ == "__main__":
    # xy_to_geojson()
    geojson_to_point()
