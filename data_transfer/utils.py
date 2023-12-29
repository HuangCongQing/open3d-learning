'''
Description: 不同格式文件读取函数合集(可根据需要选取部分函数自取)
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-26 19:45:21
LastEditTime: 2023-12-29 12:45:12
FilePath: /open3d-learning/data_transfer/utils.py
'''
import open3d as o3d  
import numpy as np
import  pickle
import os
from distutils.version import LooseVersion



# npy
def read_npy(file_path):
    points = np.load(file_path).astype(np.float32)

    return points

def save_npy(points, file_path):
    np.save(file_path, points.astype(np.float32))

# txt
def read_txt(file_path):
    # Tips：分割符根据需要修改
    first_line = None
    with open(file_path, 'r') as file:
        first_line = file.readline() # 等价于file.readlines()[0]
        # readline() 方法读取第一行数据
    if "," in first_line:
        points = np.loadtxt(file_path, delimiter=',', dtype=np.float32)
    elif " " in first_line:
        points = np.loadtxt(file_path, delimiter=' ', dtype=np.float32)
    else:
        raise  NotImplementedError("Tips：分割符根据需要修改")

    return points[:, :3]

def save_txt(points, file_path, delimiter=','):
    assert isinstance(points, np.ndarray)
    print("Tips: 默认分隔符‘,’,请根据需要修改！")
    np.savetxt(file_path, points, fmt='%f', delimiter=delimiter)  # 格式为浮点型，用“，”隔开

# bin
def read_bin(file_path, dim=3):
    assert dim ==3 or dim ==4 or dim == 6 , "请根据需要修改`dim`维度！"
    # np.fromfile 读出来的数据是一维数组，需要利用reshape指定行列信息。
    points = np.fromfile(file_path, np.float32).reshape(-1, dim)[:, :3]  # (N, 3)
    return points

def save_bin(points, file_path):
    assert isinstance(points, np.ndarray)
    # tofile函数只能将数组保存为二进制文件，文件后缀名没有固定要求。
    # 这种保存方法对数据读取有要求，np.fromfile 需要手动指定读出来的数据的的dtype，
    # 如果指定的格式与保存时的不一致，则读出来的就是错误的数据。。
    points.tofile(file_path)

# pcd
def read_pcd(file_path):
    point_cloud = o3d.io.read_point_cloud(file_path)

    # 将点云数据转换为numpy数组
    points = np.array(point_cloud.points)
    colors = np.array(point_cloud.colors)

    return points


def save_pcd(points, file_path):
    assert isinstance(points, np.ndarray)
    # 将NumPy数组转换为Open3D的PointCloud对象  
    pcd = o3d.geometry.PointCloud()  
    pcd.points = o3d.utility.Vector3dVector(points)  
    # 将PointCloud对象保存为PCD文件  
    o3d.io.write_point_cloud(file_path, pcd)

# ply
def read_ply(file_path):
    pass
def save_ply(points, file_path):
    pass


# pkl: pkl可保存 字符串、列表、字典等数据
def read_pkl(file_path):
    # # 重点是rb和r的区别，rb是打开二进制文件，r是打开文本文件
    with open(file_path,'rb') as f:
        data=pickle.load(f)
        f.close()
    # print(data)
    # print(np.array(data).shape)
    # print(type(data))
    points = np.array(data)

    return points

def save_pkl(data, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

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


if __name__ == '__main__':
    version = get_lib_version(o3d)
    file_path = "/home/chongqinghuang/code/open3d-learning/test_data/plant_0001.txt"
    points = read_txt(file_path)
    save_pcd(points, "/home/chongqinghuang/code/open3d-learning/test_data/111.pcd")
    a = read_pcd("/home/chongqinghuang/code/open3d-learning/test_data/111.pcd")
    pass