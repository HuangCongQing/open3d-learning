'''
Description: ply2stl(虽然到处没有报错，但可能还有问题) https://www.yuque.com/huangzhongqing/hre6tf/ck05ki#cteyh
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 23:42:35
LastEditTime: 2023-12-25 19:47:14
FilePath: /open3d-learning/data_transfer/ply2stl.py
'''

import open3d as o3d
import numpy as np


def get_lib_version(lib):
    print('current open3d version: ', lib.__version__)
    return lib.__version__

# https://blog.csdn.net/u014072827/article/details/112399050
def read_triangle_mesh(path):
    # 加载三角网格
    mesh = o3d.io.read_triangle_mesh(path)
    # 打印网格信息
    print(mesh)
    # 打印网格定点信息
    print('Vertices:')
    print(np.asarray(mesh.vertices))
    # 打印网格的三角形
    print('Triangles:')
    print(np.asarray(mesh.triangles))
    '''  
    Vertices:
    [[-15.61418152  39.51490784   2.21499991]
    [-15.64233303  39.52183533   2.19350004]
    [-15.60787392  39.50787354   2.19712496]
    ...
    [-15.32199955  39.56200027   0.829     ]
    [-15.33899975  39.56550217   0.4465    ]
    [-15.35999966  39.56999969   0.285     ]]
    Triangles:
    []
    
    '''

def ply_to_stl(ply_file, stl_file):
    # 读取PLY点云文件
    pcd = o3d.io.read_point_cloud(ply_file)
    # points = pcd.points
      
    # 估计法线 bugfix: [OrientNormalsToAlignWithDirection] No normals in the PointCloud. Call EstimateNormals() first.
    pcd.estimate_normals()  

    # 强制对齐法线方向  
    pcd.orient_normals_to_align_with_direction([0, 0, 1]) # 将点云对齐到z轴方向  
         
    # 计算法线  
    pcd.orient_normals_to_align_with_direction([0, 0, 1])  # 将法线对齐到z轴  
    pcd.orient_normals_towards_camera_location([0, 0, 0])  # 将法线指向相机位置（这里是一个示例，您可以根据需要进行调整）  
  

    # 创建三角网格
    mesh = o3d.geometry.TriangleMesh()
    mesh.compute_triangle_normals(normalized=False) # 计算三角形网格中每个三角形的法线，并将其存储在mesh.triangle_normals属性中。
    # mesh = o3d.geometry.TriangleMesh.compute_triangle_normals(mesh)
    mesh.vertices = o3d.utility.Vector3dVector(pcd.points)
    # mesh.triangles = o3d.utility.Vector3iVector([(1, 2, 3), (4, 5, 6), (7, 8, 9)])    # 这里需要填写自定义的三角形索引
    # mesh.triangles = o3d.utility.Vector3iVector([])    # 这里需要填写自定义的三角形索引
    # mesh.triangles = o3d.utility.Vector3iVector([(1,2,3) for i in range(np.asarray(pcd.points).shape[0])])    # 这里需要填写自定义的三角形索引


    # 添加注释
    mesh.paint_uniform_color([1, 0, 0])  # 设置三角网格颜色为红色

    # 可视化网格
    o3d.visualization.draw_geometries([mesh])
    # 保存为STL文件
    print(1111)
    o3d.io.write_triangle_mesh(stl_file, mesh)


if __name__ == '__main__':
    version = get_lib_version(o3d)
    # 使用示例
    # ply_file = '/home/hcq/pointcloud/open3d-learning/test_data/ply/conferenceRoom_1_GT.ply'   # 输入的PLY点云文件路径
    ply_file = '/home/chongqinghuang/code/open3d-learning/test_data/ply/Dragon/Dragon 2.5_ply.ply'   # 输入的PLY点云文件路径
    stl_file = 'output.stl'  # 输出的STL点云文件路径
    # read_triangle_mesh(ply_file)

    ply_to_stl(ply_file, stl_file)


'''  
ERROR: [Open3D WARNING] Write STL failed: compute normals first.
https://github.com/isl-org/Open3D/issues/2012

'''