import os
def get_data_extract():
  if "food-101" in os.listdir():
    print("Dataset already exists")
  else:
      pass
    # print("Downloading the data...")
    # !wget http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz
    # print("Dataset downloaded!")
    # print("Extracting data..")
    # !tar xzvf food-101.tar.gz
    # print("Extraction done!")