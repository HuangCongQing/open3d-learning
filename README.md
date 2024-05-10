<!--
 * @Description: open3d Point cloud processing and visualization(点云处理和可视化)
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2023-08-10 15:40:07
 * @LastEditTime: 2023-12-26 19:55:30
 * @FilePath: /open3d-learning/README.md
-->
# open3d-learning(python)
open3d Point cloud processing and visualization(点云处理和可视化)

docs: https://www.yuque.com/huangzhongqing/rx5ufe  (正在撰写，暂未公开)

> version: **open3d==0.15.2**（不同版本的API大致相同，如果运行报错，查看你当前版本对应函数）

Tips:
* 本仓库主要是python版本，c++版本，在这个[c++](c++)子文件夹里
## 1 Point cloud processing(点云处理)

* [01数据读取和加载](01数据读取和加载)
    * 读取
    * 加载
* [02数据基本操作](02数据基本操作)
    * 旋转平移（旋转矩阵和四元数）
* [03数据结构](03数据结构)
    * kdtree
    * octree
    * 最近邻搜索
    
* [04常见数据处理方法](04常见数据处理方法)
    * [AABB和OBB包围框计算](point_cloud_processing/04常见数据处理方法/计算点云包围盒与凸包.py)
    * 
* [05表面重建](05表面重建)
    * [凸包](point_cloud_processing/05表面重建/计算点云包围盒与凸包.py)
* [06体素化](06体素化)
* [07点云分割(聚类)](07点云聚类分割)
    * DBSCAN聚类
    * RANSAC平面分割
* [08特征点提取](08特征点提取)
    * ISS
    * FPFH
* [09点云配准](09点云配准)
    * ICP
* [10进阶操作实践](10进阶操作实践)
    * 目标检测任务
    * 语义分割任务
    * 加速计算
    * [01判断点云是否在凸包内](point_cloud_processing/10进阶操作实践/01判断点云是否在凸包内.py)


## 2 Visualization(可视化)

---->请参考我写的可视化模块：https://github.com/HuangCongQing/Point-Clouds-Visualization/tree/master/2open3D

- open3D [`python`]
- mayavi[`python`]
- matplolib [`python`]
- rviz(ROS) topic可视化  [`c++`][`python`]
- pcl 点云可视化 [`c++`]： [pcl-visualization可视化](https://github.com/HuangCongQing/pcl-learning/tree/master/15visualization%E5%8F%AF%E8%A7%86%E5%8C%96)


### 3 点云数据格式转换(bag|.pcd|.bin|.ply|.txt|.npy|.las|.stl|.obj)）

在Open3D库中，`read_point_cloud`函数支持读取多种点云文件格式，包括但不限于以下格式：

1. PLY (Polygon File Format)：PLY是一种常用的点云文件格式，它可以存储三维点的坐标、颜色、法线等信息。
2. ASCII格式：ASCII格式是一种简单的文本文件格式，用于存储三维点的坐标信息。
3. CSV格式：CSV是一种常见的表格数据格式，可以将三维点的坐标信息以逗号分隔的形式存储在文本文件中。
4. OFF (Object File Format)：OFF是一种用于存储三维几何数据的文件格式，可以用于存储点云数据。
5. XYZ格式：XYZ是一种简单的文本文件格式，用于存储三维点的坐标信息。

请注意，为了正确读取点云文件，需要确保文件格式与所使用的Open3D版本兼容，并且文件路径和文件名正确无误。


* doc: https://www.yuque.com/huangzhongqing/hre6tf/ck05ki
* code: [data_transfer](data_transfer)






## Plus: [Open3Dc++](c++) TODO

* TODO


## License

Copyright (c) [双愚](https://github.com/HuangCongQing). All rights reserved.

Licensed under the [MIT](./LICENSE) License.
