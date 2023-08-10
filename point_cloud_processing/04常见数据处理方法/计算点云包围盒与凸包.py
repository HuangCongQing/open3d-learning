'''
Description: 计算点云包围盒与凸包 https://www.yuque.com/huangzhongqing/rx5ufe/zdaf10s1tuzb47ey
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-09-05 21:39:27
LastEditTime: 2023-08-10 16:46:51
FilePath: /open3d-learning/point_cloud_processing/04常见数据处理方法/计算点云包围盒与凸包.py
'''

import open3d as o3d
import numpy as np


# 加载点云
pcd = o3d.io.read_point_cloud("test_data/model_chair.pcd")

# 1包围框=============================================
# 点云AABB包围盒
aabb = pcd.get_axis_aligned_bounding_box()
aabb.color = (1, 0, 0)
# 点云OBB包围盒
obb = pcd.get_oriented_bounding_box()
obb.color = (0, 1, 0)
# 可视化滤波结果
o3d.visualization.draw_geometries([pcd, aabb, obb], window_name="点云包围盒",
                                  width=800,  # 窗口宽度
                                  height=600)  # 窗口高度

# 2凸包=============================================
# 计算凸包
hull, _ = pcd.compute_convex_hull()
hull_ls = o3d.geometry.LineSet.create_from_triangle_mesh(hull)
hull_ls.paint_uniform_color((1, 0, 1))
# 可视化滤波结果
o3d.visualization.draw_geometries([pcd, hull_ls], window_name="点云凸包",
                                  width=800,  # 窗口宽度
                                  height=600)  # 窗口高度