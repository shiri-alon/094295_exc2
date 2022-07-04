import torch
import torchvision.transforms as T
from PIL import Image
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import random
import matplotlib.pyplot as plt



torch.manual_seed(20)


def add_noise(inputs, noise_factor=0.3):
    noisy = inputs + torch.randn_like(inputs) * noise_factor
    noisy = torch.clip(noisy, 0., 1.)
    return noisy


directory = '/home/student/HW2/data/train'
dirs = next(os.walk(directory))[1]
print(dirs)

for dir in dirs:
    dir_source_path = '/home/student/HW2/data/train/' + dir

    files = [f for f in listdir(dir_source_path) if isfile(join(dir_source_path, f))]
    print(dir)
    print(len(files))

    for image_name in random.sample(files, int(len(files) * .5)):
        origin_path = dir_source_path + '/' + image_name
        dest_path = dir_source_path + '/' + image_name.split(".png")[0] + "_aug_noise.png"
        orig_img = Image.open(Path(origin_path))

        noise_img = add_noise(T.ToTensor()(orig_img), random.uniform(0.3, 0.45))
        noise_img = T.ToPILImage()(noise_img)
        noise_img.save(dest_path)


