'''
Description: 不同格式文件读取函数合集(可根据需要选取部分函数自取)
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-26 19:45:21
LastEditTime: 2023-12-29 11:45:25
FilePath: /open3d-learning/data_transfer/utils.py
'''
import open3d as o3d  
import numpy as np
from distutils.version import LooseVersion

# txt
def read_txt(file_path):
    pass
def save_txt(points, file_path):
    pass

# pcd
def read_pcd(file_path):
    pass
def save_pcd(points, file_path):
    pass

# ply
def read_ply(file_path):
    pass
def save_ply(points, file_path):
    pass



def get_lib_version(lib):
    print('current open3d version: ', lib.__version__)
    return lib.__version__

# version = get_lib_version(o3d)
# print("Tips: 读取txt文件函数只在v0.14及其以上版本存在！！！")
# # ===========================
# input_path = "/home/hcq/pointcloud/open3d-learning/test_data/plant_0001.txt"
# output_path = "output.pcd"
# # if "0.15" in o3d.__version__:
# if LooseVersion(version)  >= "0.14.0":
#     pass
# else:
#     raise NotImplementedError("请查看open3d版本，确定`read_points_from_text`函数是否存在或变更")