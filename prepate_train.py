# Prepare train dataset by copying images from food-101/images to food-101/train using the file train.txt
import util
print("Creating train data...")
util.prepare_data('food-101/meta/train.txt', 'food-101/images', 'train')