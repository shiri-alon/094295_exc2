
import random
import os
import shutil
from os import listdir
from os.path import isfile, join

if __name__ == '__main__':

    directory = '/home/student/HW2/data/train'
    dirs = next(os.walk(directory))[1]
    print(dirs)

    for dir in dirs:
        dir_source_path = '/home/student/HW2/data/train/' + dir
        dir_dest_path = '/home/student/HW2/data/val/' + dir

        files = [f for f in listdir(dir_source_path) if isfile(join(dir_source_path, f))]
        print(dir)
        print(len(files))

        for image_name in random.sample(files, int(len(files) * .1)):
            from_path = dir_source_path + '/' + image_name
            dest_path = dir_dest_path + '/' + image_name
            os.rename(from_path, dest_path)

        files = [f for f in listdir(dir_source_path) if isfile(join(dir_source_path, f))]
        print(len(files))
        print("\n")
