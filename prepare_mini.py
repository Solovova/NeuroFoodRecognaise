import util

# picking 3 food items and generating separate data folders for the same
food_list = ['samosa','pizza','omelette']
src_train = 'train'
dest_train = 'train_mini'
src_test = 'test'
dest_test = 'test_mini'

print("Creating train data folder with new classes")
util.dataset_mini(food_list, src_train, dest_train)
util.dataset_mini(food_list, src_test, dest_test)
