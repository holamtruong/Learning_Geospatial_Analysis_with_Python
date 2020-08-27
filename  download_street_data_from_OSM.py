import osmnx as ox

# download street data from OSM for a city, creates a street network from it, and calculates some basic statistics:
def download_street():
    # G = ox.graph_from_place('Bay Saint Louis, MS , USA', network_type='drive')
    G = ox.graph_from_place('Quận 1, Thành phố Hồ Chí Minh , VN', network_type='drive')
    stats = ox.basic_stats(G)
    len_street = stats["street_length_avg"]
    print(len_street)


if __name__ == "__main__":
    download_street()
