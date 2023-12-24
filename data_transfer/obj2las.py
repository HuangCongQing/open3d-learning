'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 16:48:39
LastEditTime: 2023-12-24 19:42:43
FilePath: /open3d-learning/data_transfer/obj2las.py
'''
import open3d as o3d
import numpy as np

def convert_obj_to_las(obj_file, las_file):
    # 读取 obj 文件
    obj = o3d.io.read_triangle_mesh(obj_file)

    # 获取顶点坐标
    vertices = np.asarray(obj.vertices)

    # 创建点云对象
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(vertices)

    # 保存为 las 文件
    o3d.io.write_point_cloud(las_file, point_cloud)

# 示例：将 obj 文件转换为 las 文件
obj_file = "../test_data/obj/FinalBaseMesh.obj"
las_file = "../test_data/obj/FinalBaseMesh_output.las"
convert_obj_to_las(obj_file, las_file)

'''  
issue: https://github.com/isl-org/Open3D/issues/3166
[Open3D WARNING] Unable to load file ../test_data/obj/FinalBaseMesh.obj with ASSIMP
[Open3D WARNING] Write geometry::PointCloud failed: unknown file extension las for file ../test_data/obj/FinalBaseMesh_output.las.
'''