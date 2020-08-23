# Python's StringIO module to temporarily store data in memory in a file-like object that implements various methods
import urllib.request
import urllib.parse
import urllib.error
import zipfile
import io
import struct
url = "https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"
cloudshape = urllib.request.urlopen(url)
memoryshape = io.BytesIO(cloudshape.read())
zipshape = zipfile.ZipFile(memoryshape)
cloudshp = zipshape.read("hancock.shp")
# Access Python string as an array
struct.unpack("<dddd", cloudshp[36:68])
(-89.6904544701547, 30.173943486533133, -89.32227546981174,
30.6483914869749)
