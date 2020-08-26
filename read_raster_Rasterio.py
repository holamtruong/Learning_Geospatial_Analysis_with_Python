import rasterio


def read_raster():
    raster = rasterio.open("sample_data\SatImage\SatImage.tif")
    ras_name = raster.name
    number_band = raster.count
    xsize = raster.width
    ysize = raster.height

    print(ras_name, number_band, xsize, ysize)


if __name__ == "__main__":
    read_raster()
