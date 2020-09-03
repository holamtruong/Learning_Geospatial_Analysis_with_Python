# this code is the copy from Mr.soiqualang

from osgeo import ogr
from osgeo import gdal
import subprocess

shp = 'E:/DEV/Learning_Geospatial_Analysis_with_Python/sample_data/bentre_data/bentre_town.shp'

inRaster = 'sample_data/bentre_data/bentre_landsat.tif'
outRaster = 'sample_data/bentre_data/output_bentre_town1.tif'

inRaster2 = 'sample_data/bentre_data/bentre_landsat_extend.tif'
outRaster2 = 'sample_data/bentre_data/output_bentre_town2.tif'

inRaster3 = 'sample_data/bentre_data/bentre_man_s1_20191115.tif'
outRaster3 = 'sample_data/bentre_data/output_bentre_town3.tif'

def clip(shp, inRaster, outRaster):
    print(shp)
    print(inRaster)
    print(outRaster)

    cmdLine2 = "gdalwarp -cutline " + shp + " -crop_to_cutline -of Gtiff -dstnodata -9999 -overwrite " + inRaster + ' ' + outRaster

    p1 = subprocess.Popen(cmdLine2, shell=True)
    p1.wait()
    return outRaster


clip(shp, inRaster, outRaster)
# clip(shp, inRaster2, outRaster2)
# clip(shp, inRaster3, outRaster3)
