'''
Description: obj2las(若有问题，根据需要调整维度)
参考: https://blog.csdn.net/technology_cat/article/details/114841707
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-12-24 16:48:39
LastEditTime: 2023-12-24 23:37:27
FilePath: /open3d-learning/data_transfer/obj2las.py
'''
import open3d as o3d
import numpy as np
import laspy


def convert_obj_to_las(obj_file, las_file):
    # 读取 obj 文件
    obj = o3d.io.read_triangle_mesh(obj_file)

    # 获取顶点坐标
    vertices = np.asarray(obj.vertices)

    # 创建点云对象
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(vertices)

    # 保存为 las 文件
    o3d.io.write_las_point_cloud(las_file, point_cloud)

# https://blog.csdn.net/u014311125/article/details/118338518#t12
# 以x y z r g b的方式定义点云数据
def save_las(points, save_las_file):
    # save_las_file = r"save_las.las"

    # 以x y z r g b的方式定义点云数据
    # points = np.array([[8, 5, 3, 255, 0, 0],
    #                     [9, 0, 1, 255, 0, 0],
    #                     [2, 5, 3, 0, 255, 0],
    #                     [0, 4, 2, 0, 255, 0],
    #                     [7, 2, 9, 0, 0, 255],
    #                     [8, 8, 4, 0, 0, 255],
    #                     [9, 5, 8, 255, 0, 255],
    #                     [2, 5, 9, 255, 0, 255],
    #                     [0, 7, 5, 255, 255, 0],
    #                     [11, 2, 8, 255, 255, 0],
    #                     [10, 9, 0, 255, 255, 0]
    #                     ])

    if points.shape[1] < 6:
        N = points.shape[0]
        C = 3
        points = np.concatenate((points[:, :3], np.zeros((N, C))), axis=1)

    # 创建点云文件
    try:
        las = laspy.create(file_version="1.2", points_format=3)
    except Exception as err:
        # print(err)
        las = laspy.create(file_version="1.2", point_format=3)
    las.x = points[:, 0]
    las.y = points[:, 1]
    las.z = points[:, 2]
    las.red = points[:, 3]
    las.green = points[:, 4]
    las.blue = points[:, 5]

    # 保存las文件
    las.write(save_las_file)

# 参考: https://blog.csdn.net/technology_cat/article/details/114841707
def load_obj(obj_path, isGetStructure=False):
    points = []
    face_vertex = []  # 面部顶点
    face_normal = []  # 面部法向量
    face_texture = []  # 面部纹理
    vt = []  # 纹理坐标
    vn = []  # 顶点法向量
    fvt = []  #
    triangled = []  # 四边形划分的三角形

    with open(obj_path) as file:
        while 1:
            line = file.readline()
            sfv1 = []
            sfv2 = []
            sfvt1 = []
            sfvt2 = []
            sfvn1 = []
            sfvn2 = []

            xyz1 = []
            xyz2 = []

            if not line:
                break
            # olderror:  strs = line.strip().split(" ")  # 读取到的数据
            strs = ' '.join(line.strip().split()).split(" ")
            if strs[0] == "v":
                points.append(np.array([float(strs[1]), float(strs[2]), float(strs[3])]))
            if isGetStructure and strs[0] == "vt":
                vt.append([float(strs[1]), float(strs[2])])
            if isGetStructure and strs[0] == "vn":
                vn.append([float(strs[1]), float(strs[2]), float(strs[3])])
            if isGetStructure and strs[0] == "f":
                for i in range(1, len(strs)):  # 将四边形切分为三角面片
                    dum = strs[i].split("/")
                    if (i != 4):
                        sfv1.append(int(dum[0]))
                        sfvt1.append(int(dum[1]))
                        sfvn1.append(int(dum[2]))

                    if (i != 2):
                        sfv2.append(int(dum[0]))
                        sfvt2.append(int(dum[1]))
                        sfvn2.append(int(dum[2]))

                if (len(strs) == 5):

                    face_vertex.append(sfv1)
                    face_texture.append(sfvt1)
                    face_normal.append(sfvn1)
                    triangled.append(False)

                    face_vertex.append(sfv2)
                    face_texture.append(sfvt2)
                    face_normal.append(sfvn2)
                    triangled.append(False)

                else:
                    face_vertex.append(sfv1)
                    face_texture.append(sfvt1)
                    face_normal.append(sfvn1)
                    triangled.append(True)

    if isGetStructure:
        return points, face_vertex, face_normal, face_texture, vn, vt, triangled
    else:
        return points

def get_lib_version(lib):
    print('current open3d version: ', lib.__version__)
    return lib.__version__


if __name__ == '__main__':
    version = get_lib_version(o3d)
    # ===========================
    # 示例：将 obj 文件转换为 las 文件
    obj_file = "/home/hcq/pointcloud/open3d-learning/test_data/obj/FinalBaseMesh.obj"
    las_file = r"FinalBaseMesh_output.las"
    # convert_obj_to_las(obj_file, las_file)
    points = load_obj(obj_file)
    # list转成numpy.reshape(-1, 3)
    points = np.array([x for x in points ]).reshape(-1, 3)# (x,y,z)
    save_las(points, las_file)



'''  
issue: https://github.com/isl-org/Open3D/issues/3166
[Open3D WARNING] Unable to load file ../test_data/obj/FinalBaseMesh.obj with ASSIMP
[Open3D WARNING] Write geometry::PointCloud failed: unknown file extension las for file ../test_data/obj/FinalBaseMesh_output.las.
'''