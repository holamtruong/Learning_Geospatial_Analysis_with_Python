import json

jsdata = '''{
    "type": "Feature",
    "id": "OpenLayers.Feature.Vector_314",
    "properties": {},
    "geometry": {
        "type": "Point",
        "coordinates": [
            97.03125,
            39.7265625
        ]
    },
    "crs": {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    }
}'''


def string_to_JSON(jsdata):
    a = json.loads(jsdata)
    # print(a)
    return a


def JSON_to_string(jsdata):
    json_obj = string_to_JSON(jsdata)
    # string = json.dumps(json_obj)
    string = json.dumps(json_obj, indent=4)  # indent to easy read
    print(string)


if __name__ == "__main__":
    # string_to_JSON(jsdata)
    JSON_to_string(jsdata)
