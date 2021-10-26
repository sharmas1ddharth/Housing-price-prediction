import os
import requests

DOWNLOADING_PATH = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
DATASET_PATH = "data/raw/"

def fetch_data(download_url, save_location):
    """
    function to download dataset
    """
    if not os.path.isdir(save_location):
        os.makedirs(save_location)
    r = requests.get(download_url)
    content = r.content
    csv_file = open(f"{save_location}/data.csv", 'wb')
    csv_file.write(content)
    csv_file.close()
    
    
if __name__ == "__main__":
    fetch_data(DOWNLOADING_PATH, DATASET_PATH)