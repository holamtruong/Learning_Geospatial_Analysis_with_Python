import urllib.request
import urllib.parse
import urllib.error
import requests

def get_github_file():
    url = "https://github.com/GeospatialPython/Learn/raw/master/hancock.zip"
    fileName = "hancock.zip"
    temp_file = urllib.request.urlretrieve(url, fileName) #download to local
    print(temp_file)
    # return ('hancock.zip', <http.client.HTTPMessage object at 0x03E6F598>)


def get_earthquake_data():
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"
    earthquakes = urllib.request.urlopen(url)
    for record in earthquakes:
        print(record)

def get_data_req():
    url = "https://github.com/GeospatialPython/Learning/raw/master/hancock.zip"
    fileName = "hancock.zip"
    r = requests.get(url)
    print(r.content)
    with open(fileName, 'wb') as f:
        f.write(r.content)


if __name__ == "__main__":
    # get_github_file()
    # get_earthquake_data()
    get_data_req()

