'''
Description: stl2ply https://www.yuque.com/huangzhongqing/hre6tf/ck05ki#cteyh
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 23:42:35
LastEditTime: 2023-12-24 23:51:17
FilePath: /open3d-learning/data_transfer/stl2ply.py
'''
import open3d as o3d

def stl_to_ply(stl_file, ply_file):
    # 读取STL点云文件
    mesh = o3d.io.read_triangle_mesh(stl_file)

    # 提取点云数据
    pcd = mesh.sample_points_poisson_disk(10000)  # 使用Poisson-Disk采样提取点云数据

    # 添加注释
    colors = [[1, 0, 0] for _ in range(pcd.points.shape[0])]  # 创建红色注释
    pcd.colors = o3d.utility.Vector3dVector(colors)  # 设置点云注释

    # 保存为ply文件
    o3d.io.write_point_cloud(ply_file, pcd)

# 使用示例
stl_file = '/home/hcq/pointcloud/open3d-learning/data_transfer/output.stl'   # 输入的STL点云文件路径
ply_file = 'output.ply'  # 输出的PLY点云文件路径

stl_to_ply(stl_file, ply_file)
