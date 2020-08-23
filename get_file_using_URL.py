import urllib.request
import urllib.parse
import urllib.error


def get_github_file():
    url = "https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"
    fileName = "hancock.zip"
    temp_file = urllib.request.urlretrieve(url, fileName)
    print(temp_file)
    # return ('hancock.zip', <http.client.HTTPMessage object at 0x03E6F598>)


def get_earthquake_data():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"
    earthquakes = urllib.request.urlopen(url)
    earthquakes.readline()
    'time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place\n'
    earthquakes.readline()
    '2013-06-14T14:37:57.000Z,64.8405,-147.6478,13.1,0.6,Ml,6,180,0.09701805,0.2,ak,ak10739050,2013-06-14T14:39:09.442Z,"3km E of Fairbanks,Alaska"\n'


if __name__ == "__main__":
    get_github_file()
    get_earthquake_data()
