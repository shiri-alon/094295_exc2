import torch
import torchvision.transforms as T
from PIL import Image
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import random
import matplotlib.pyplot as plt

torch.manual_seed(21)

directory = '/home/student/HW2/data/train'
dirs = next(os.walk(directory))[1]
print(dirs)

for dir in dirs:
    dir_source_path = '/home/student/HW2/data/train/' + dir

    files = [f for f in listdir(dir_source_path) if isfile(join(dir_source_path, f))]
    print(dir)
    print(len(files))

    for image_name in files:
        origin_path = dir_source_path + '/' + image_name
        dest_path = dir_source_path + '/' + image_name.split(".png")[0] + "_aug_blur.png"
        orig_img = Image.open(Path(origin_path))

        blurred_img = T.GaussianBlur(kernel_size=(51, 91), sigma=(3, 4))(orig_img)


        blurred_img.save(dest_path)







