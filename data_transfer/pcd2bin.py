'''
Description: pcd2bin(根据需要调整维度)
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 21:36:36
LastEditTime: 2023-12-24 22:08:26
FilePath: /open3d-learning/data_transfer/pcd2bin.py
'''

import open3d as o3d  
import numpy as np

print('current open3d version: ', o3d.__version__)

# 使用open3d进行读取，并扩展0到第四维度，然后转为二进制bin文件
def read_pcd(filepath):
    lidar = []
    pcd = o3d.io.read_point_cloud(filepath, format='pcd')
    points = np.array(pcd.points)
    for linestr in points:
        if len(linestr) == 3:  # only x,y,z
            linestr_convert = list(map(float, linestr))
            linestr_convert.append(0)
            lidar.append(linestr_convert)
        if len(linestr) == 4:  # x,y,z,i
            linestr_convert = list(map(float, linestr))
            lidar.append(linestr_convert)
    return np.array(lidar)

def pcd2bin(pcd_fullname, bin_fullname):
    pl = read_pcd(pcd_fullname)
    # 根据需要调整维度
    pl = pl.reshape(-1, 4).astype(np.float32)  # x,y,z,i
    pl.tofile(bin_fullname)

    

if __name__ == '__main__':
    # 读取点云数据  
    input_path = "/home/hcq/pointcloud/open3d-learning/test_data/pcd/table.pcd"
    output_path = "output.bin"
    pcd2bin(input_path, output_path)
    print("tranfer done!")