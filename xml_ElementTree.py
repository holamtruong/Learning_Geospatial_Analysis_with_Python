import xml.etree.ElementTree as ET


def read_xml():
    tree = ET.ElementTree(file="sample_data/time-stamp-point.kml")
    ns = "{http://www.opengis.net/kml/2.2}"
    placemark = tree.find(".//%sPlacemark" % ns)
    coordinates = placemark.find("./{}Point/{}coordinates".format(ns, ns))
    a = coordinates.text
    print(a)

    # -122.536226,37.86047,0


def write_xml():
    root = ET.Element("kml")
    root.attrib["xmlns"] = "http://www.opengis.net/kml/2.2"
    placemark = ET.SubElement(root, "Placemark")
    office = ET.SubElement(placemark, "name")
    office.text = "Office"
    point = ET.SubElement(placemark, "Point")
    coordinates = ET.SubElement(point, "coordinates")
    coordinates.text = "-122.087461,37.422069, 37.422069"
    tree = ET.ElementTree(root)
    tree.write("placemark.kml", xml_declaration=True, encoding='utf-8', method="xml")


if __name__ == "__main__":
    write_xml()
