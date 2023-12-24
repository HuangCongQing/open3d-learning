'''
Description: stl2ply https://www.yuque.com/huangzhongqing/hre6tf/ck05ki#cteyh
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 23:42:35
LastEditTime: 2023-12-25 01:07:08
FilePath: /open3d-learning/data_transfer/stl2ply.py
'''
import open3d as o3d

def stl_to_ply(stl_file, ply_file):
    # 读取STL点云文件
    mesh = o3d.io.read_triangle_mesh(stl_file)

     # 将网格保存为 PLY 文件  
    o3d.io.write_triangle_mesh(ply_file, mesh) 

# 使用示例
stl_file = '/home/hcq/pointcloud/open3d-learning/test_data/stl/Dragon/Dragon 2.5_stl.stl'   # 输入的STL点云文件路径
ply_file = 'output.ply'  # 输出的PLY点云文件路径

stl_to_ply(stl_file, ply_file)
