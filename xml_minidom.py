from xml.dom import minidom

kml = minidom.parse("sample_data/time-stamp-point.kml")
Placemarks = kml.getElementsByTagName("Placemark")
a = len(Placemarks)
print(a)


b = Placemarks[0].toxml()
print(b)
