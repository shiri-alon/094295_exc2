
import random
import os
import shutil
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':

    directory = '/home/student/HW2/data/train'
    dirs = next(os.walk(directory))[1]
    num_train = 0
    for dir in dirs:
        dir_source_path = '/home/student/HW2/data/train/' + dir

        files = [f for f in listdir(dir_source_path) if isfile(join(dir_source_path, f))]
        num_train += len(files)

    print(f"train: {num_train}")

    directory = '/home/student/HW2/data/val'
    dirs = next(os.walk(directory))[1]
    num_val = 0
    for dir in dirs:
        dir_source_path = '/home/student/HW2/data/val/' + dir

        files = [f for f in listdir(dir_source_path) if isfile(join(dir_source_path, f))]
        num_val += len(files)

    print(f"val: {num_val}")
    print(f"total: {num_val + num_train}")
    print(f"can add {10000 - num_val - num_train}")
