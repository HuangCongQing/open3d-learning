'''
Description: pcd2txt
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 21:36:36
LastEditTime: 2023-12-24 21:51:46
FilePath: /open3d-learning/data_transfer/pcd2txt.py
'''
import open3d as o3d
import numpy as np

# 读取pcd点云文件
point_cloud = o3d.io.read_point_cloud("/home/hcq/pointcloud/open3d-learning/test_data/pcd/table.pcd")

# # 将点云数据转换为numpy数组
points = np.asarray(point_cloud.points)
colors = np.asarray(point_cloud.colors)

#将点云数据保存为txt文件（根据需要保存！）
#第一个参数是要保存的文件名
#第二参数是要保存的array
# delimiter：分隔符，默认为逗号，可以自己指定
# fmt：保存的数据格式

# only 保存points
np.savetxt("output.txt", points, delimiter=" ", fmt="%.6f %.6f %.6f")

# 保存points和colors
# np.savetxt("output.txt", np.hstack((points, colors)), delimiter=" ", fmt="%.6f %.6f %.6f %d %d %d")


# 将点云数据写入 txt 文件  
# with open("output.txt", "w") as f:
#     for i, point in enumerate(points):
#         f.write(f"Point {i}: {point.x}, {point.y}, {point.z}\n")


'''  
Tips:
从txt文件中读取数据
b=np.loadtxt('a.txt',dtype=np.float32)
'''