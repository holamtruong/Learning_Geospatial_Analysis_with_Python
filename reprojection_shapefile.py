# shutil module is used to copy .dbf
# the Open Spatial Reference module, also known as osr
from osgeo import ogr
from osgeo import osr
import os
import shutil


# reprojection 'New York 3104' to 'WGS84'
def reprojection_shp():
    # 1. Define our shapefile names as variables:
    srcName = 'sample_data/reprojection_data/NYC_MUSEUMS_LAMBERT.shp'
    tgtName = 'sample_data/reprojection_data/NYC_MUSEUMS_GEO.shp'

    # 2. Create our target spatial reference using the osr module as EPSG code 4326, which is WGS84 Geographic:
    tgt_spatRef = osr.SpatialReference()
    tgt_spatRef.ImportFromEPSG(4326)  # 'GEOGCS["WGS 84", DATUM["WGS_1984",...]'

    # 3.  Set up input shapefile Reader object using ogr and get the spatial reference:
    driver = ogr.GetDriverByName('ESRI Shapefile')  # get driver
    src = driver.Open(srcName, 0)  # open file
    srcLyr = src.GetLayer()
    src_spatRef = srcLyr.GetSpatialRef()  # 'PROJCS["New York 3104, Long Island Zone [1983,...]

    # 4. Check whether our target shapefile already exists from a previous test run and delete it if it does:
    if os.path.exists(tgtName):
        driver.DeleteDataSource(tgtName)

    # 5. Build our target layer for the shapefile:
    tgt = driver.CreateDataSource(tgtName)
    lyrName = os.path.splitext(tgtName)[0]  # sample_data/reprojection_data/NYC_MUSEUMS_GEO

    # Use well-known binary format (WKB) to specify geometry
    tgtLyr = tgt.CreateLayer(lyrName, geom_type=ogr.wkbPoint)
    featDef = srcLyr.GetLayerDefn()
    trans = osr.CoordinateTransformation(src_spatRef, tgt_spatRef)

    # 5.  We can loop through the features in our source shapefile, reproject them using the Transform() method, and add them to the new shapefile:
    srcFeat = srcLyr.GetNextFeature()
    while srcFeat:
        geom = srcFeat.GetGeometryRef()  # POINT (980435.999939421 195695.999993801)
        geom.Transform(trans)  # POINT (40.7038165500454 -74.0137557957376)
        feature = ogr.Feature(featDef)
        feature.SetGeometry(geom)
        tgtLyr.CreateFeature(feature)
        feature.Destroy()
        srcFeat.Destroy()
        srcFeat = srcLyr.GetNextFeature()
    src.Destroy()
    tgt.Destroy()

    # 6. Convert geometry to Esri flavor of Well-Known Text (WKT) format for export to the projection (prj) file
    tgt_spatRef.MorphToESRI()
    prj = open(lyrName + '.prj', 'w')  # sample_data/reprojection_data/NYC_MUSEUMS_GEO.prj
    prj.write(tgt_spatRef.ExportToWkt())  # GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984"...]
    prj.close()

    # 7. Make a copy of the .dbf source with the new filename as the attributes are part of the reprojection process:
    srcDbf = os.path.splitext(srcName)[0] + '.dbf'  # sample_data/reprojection_data/NYC_MUSEUMS_GEO.dbf
    tgtDbf = lyrName + '.dbf'
    shutil.copyfile(srcDbf, tgtDbf)


if __name__ == "__main__":
    reprojection_shp()
