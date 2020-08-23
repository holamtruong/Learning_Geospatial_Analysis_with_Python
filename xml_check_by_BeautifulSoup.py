# pip install beautifulsoup4
from bs4 import BeautifulSoup


def read_xml_by_bs4():
    gpx = open("sample_data/broken_data.gpx")
    soup = BeautifulSoup(gpx.read(), features="xml")


if __name__ == "__main__":
    read_xml_by_bs4()
