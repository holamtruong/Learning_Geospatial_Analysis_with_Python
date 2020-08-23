import zipfile

def zipfile_name():
    zip = open("sample_data/hancock.zip", "rb")
    zipShape = zipfile.ZipFile(zip)
    shpName, shxName, dbfName = zipShape.namelist()
    shpFile = open(shpName, "wb")
    shxFile = open(shxName, "wb")
    dbfFile = open(dbfName, "wb")
    shpFile.write(zipShape.read(shpName))
    shxFile.write(zipShape.read(shxName))
    dbfFile.write(zipShape.read(dbfName))
    shpFile.close()
    shxFile.close()
    dbfFile.close()

def zipfile_name_loop():
    zip = open("sample_data/hancock.zip", "rb")
    zipShape = zipfile.ZipFile(zip)
    for fileName in zipShape.namelist():
        out = open(fileName, "wb")
        out.write(zipShape.read(fileName))
        out.close()

if __name__ == "__main__":
    zipfile_name_loop()
