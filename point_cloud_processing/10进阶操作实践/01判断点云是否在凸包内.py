'''
Description: 我们使用compute_convex_hull()方法计算点云的凸包。https://www.yuque.com/huangzhongqing/rx5ufe/zdaf10s1tuzb47ey#zqca3
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-08-10 16:56:09
LastEditTime: 2023-08-10 17:28:47
FilePath: /open3d-learning/point_cloud_processing/10进阶操作实践/01判断点云是否在凸包内.py
'''

import numpy as np
import open3d as o3d

# 将点云转换为Open3D的PointCloud对象
def array_to_pointcloud(points):
    # 将点云转换为Open3D的PointCloud对象
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(points)
    return cloud


def conv_hull(points: np.ndarray):
    """
    生成凸包 参考文档：https://blog.csdn.net/io569417668/article/details/106274172
    :param points: 待生成凸包的点集
    :return: 索引 list
    """

    # 将点云转换为Open3D的PointCloud对象
    cloud1 = array_to_pointcloud(points)
    # 凸包
    hull, lst = cloud1.compute_convex_hull()
    return lst
    '''
	这里的load_data_txt是我自己写的函数，主要是读入三维点坐标，返回list
	array_to_point_cloud是用来把NdArray类型的点坐标转换成o3d.geometry.PointCloud类型的函数
    '''


# 这里会返回列表类型
def load_data_txt(path):
    file = open(path, 'r')
    data = file.read().split('\n')
    lst = _data_trans(data)
    return lst


def array_to_pointcloud(np_array):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np_array)
    return pcd


def _data_trans(data):
    lst = []
    for num in data:
        num_list = num.split()
        lst.append([eval(i) for i in num_list])
    lst.pop()
    return lst

# 下面是检测点是否在凸包内的函数：
def in_convex_polyhedron(points_set: np.ndarray, test_points: np.ndarray):
    """
    检测点是否在凸包内
    :param points_set: 凸包，需要对分区的点进行凸包生成 具体见conv_hull函数
    :param test_points: 需要检测的点 可以是多个点
    :return: bool类型
    """
    assert type(points_set) == np.ndarray
    assert type(points_set) == np.ndarray
    bol = np.zeros((test_points.shape[0], 1), dtype=np.bool)
    ori_set = points_set
    ori_edge_index = conv_hull(ori_set)
    ori_edge_index = np.sort(np.unique(ori_edge_index))
    for i in range(test_points.shape[0]):
        new_set = np.concatenate((points_set, test_points[i, np.newaxis]), axis=0)
        new_edge_index = conv_hull(new_set)
        new_edge_index = np.sort(np.unique(new_edge_index))
        bol[i] = (new_edge_index.tolist() == ori_edge_index.tolist())
    return bol

if __name__ == '__main__':
    # test1
    A = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1],
                  [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])

    p = np.array([[.5, .5, .5], [.2, .3, .6], [1, 1, 1.1]])
    print(in_convex_polyhedron(A, p))  # True True False

    # test2
    # path = r'D:\desktop\data\lower_jaw_data\points1.txt'
    # points_set = np.array(load_data_txt(path))
    # p = np.array([[2.31740, -0.72062, 12.51270], [115, 115, 115]])
    # print(in_convex_polyhedron(points_set, p))  # True, False