from osgeo import gdal


def read_raster():
    raster = gdal.Open("sample_data\SatImage\SatImage.tif")
    number_band = raster.RasterCount
    xsize = raster.RasterXSize
    ysize = raster.RasterYSize

    print(number_band, xsize, ysize)


if __name__ == "__main__":
    read_raster()
