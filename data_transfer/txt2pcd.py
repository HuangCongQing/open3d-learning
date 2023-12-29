'''
Description: txt2pcd(根据需要调整维度)
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 21:36:36
LastEditTime: 2023-12-29 12:49:17
FilePath: /open3d-learning/data_transfer/txt2pcd.py
'''

import open3d as o3d  
import numpy as np
from distutils.version import LooseVersion
from utils import *
def get_lib_version(lib):
    print('current open3d version: ', lib.__version__)
    return lib.__version__

def txt2pcd(input_path, output_path):
    # 读取txt点云文件
    points = read_txt(input_path)
    # 保存为pcd点云文件
    save_pcd(points, output_path)

if __name__ == '__main__':
    version = get_lib_version(o3d)
    # ===========================
    input_path = "/home/hcq/pointcloud/open3d-learning/test_data/plant_0001.txt"
    output_path = "output.pcd"
    txt2pcd(input_path, output_path)
    