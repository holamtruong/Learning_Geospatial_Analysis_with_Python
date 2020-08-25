# pip install beautifulsoup4
# pip install lxml
from bs4 import BeautifulSoup


def read_xml_by_bs4():
    gpx = open("sample_data/broken_data.gpx")
    soup = BeautifulSoup(gpx.read(), features="xml")
    print(soup.trkpt)
    tracks = soup.findAll("trkpt")
    print(len(tracks))
    # print(soup.prettify())


if __name__ == "__main__":
    read_xml_by_bs4()


