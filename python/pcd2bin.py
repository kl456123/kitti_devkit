# -*- coding: utf-8 -*-

import os

# 定义一个三维点类

import numpy as np

pcd_dir = "../"

bin_dir = "../velodyne"

if not os.path.isdir(bin_dir):
    os.mkdir(bin_dir)

for filename in os.listdir(pcd_dir):
    if not os.path.splitext(filename)[1] == ".pcd":
        continue
    points = []
    with open(os.path.join(pcd_dir, filename)) as f:
        for idx, line in enumerate(f.readlines()):
            if idx < 11:
                print(line)
                continue
            data = line.split(' ')
            data = [float(item) for item in data]
            points.append(data)

    points = np.array(points, dtype=np.float32).reshape((-1, 4))
    points.tofile(
        os.path.join(bin_dir,
                     os.path.splitext(filename)[0] + ".bin"))
    print("file :{} has been convert to bin and saved!".format(filename))
