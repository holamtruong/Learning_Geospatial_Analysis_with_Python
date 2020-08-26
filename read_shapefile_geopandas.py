# python -m pip install -U matplotlib
import geopandas
import matplotlib.pyplot as plt


def read_shp():
    gdf = geopandas.GeoDataFrame
    census = gdf.from_file("sample_data\GIS_CensusTract\GIS_CensusTract_poly.shp")
    print(census)



if __name__ == "__main__":
    read_shp()
