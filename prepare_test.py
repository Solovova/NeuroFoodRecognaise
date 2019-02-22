# Prepare test data by copying images from food-101/images to food-101/test using the file test.txt
import util

print("Creating test data...")
util.prepare_data('food-101/meta/test.txt', 'food-101/images', 'test')