'''
Description: txt2pcd(根据需要调整维度)
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 21:36:36
LastEditTime: 2023-12-26 19:38:21
FilePath: /open3d-learning/data_transfer/txt2pcd.py
'''

import open3d as o3d  
import numpy as np
from distutils.version import LooseVersion



def get_lib_version(lib):
    print('current open3d version: ', lib.__version__)
    return lib.__version__

def txt2pcd(input_path, output_path):
    # 读取txt点云文件
    txt_point_cloud = o3d.io.read_point_cloud(input_path, format='xyzrgb')
    # 保存为pcd点云文件
    o3d.io.write_point_cloud(output_path, txt_point_cloud)

if __name__ == '__main__':
    version = get_lib_version(o3d)
    print("Tips: 读取txt文件函数只在v0.14及其以上版本存在！！！")
    # ===========================
    input_path = "/home/hcq/pointcloud/open3d-learning/test_data/plant_0001.txt"
    output_path = "output.pcd"
    # if "0.15" in o3d.__version__:
    if LooseVersion(version)  >= "0.14.0":
        txt2pcd(input_path, output_path)
    else:
        raise NotImplementedError("请查看open3d版本，确定`read_points_from_text`函数是否存在或变更")