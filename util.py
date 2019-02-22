# Helper method to split dataset into train and test folders
import os
from shutil import copy
from collections import defaultdict
from shutil import copytree, rmtree


def prepare_data(filepath, src, dest):
    classes_images = defaultdict(list)
    with open(filepath, 'r') as txt:
        paths = [read.strip() for read in txt.readlines()]
        for p in paths:
            food = p.split('/')
            classes_images[food[0]].append(food[1] + '.jpg')

    for food in classes_images.keys():
        print("\nCopying images into ", food)
        if not os.path.exists(os.path.join(dest, food)):
            os.makedirs(os.path.join(dest, food))
        for i in classes_images[food]:
            copy(os.path.join(src, food, i), os.path.join(dest, food, i))
    print("Copying Done!")

    # Helper method to create train_mini and test_mini data samples


def dataset_mini(food_list, src, dest):
    if os.path.exists(dest):
        # removing dataset_mini(if it already exists) folders so that we will have only the classes that we want
        rmtree(dest)
    os.makedirs(dest)
    for food_item in food_list:
        print("Copying images into", food_item)
        copytree(os.path.join(src, food_item), os.path.join(dest, food_item))
