import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("point_cloud.ply")
pcd.estimate_normals()

# to obtain a consistent normal orientation
pcd.orient_normals_towards_camera_location(pcd.get_center())

# or you might want to flip the normals to make them point outward, not mandatory
pcd.normals = o3d.utility.Vector3dVector( - np.asarray(pcd.normals))

mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=4)

# Save mesh to file
o3d.io.write_triangle_mesh("pcd.gltf", mesh)


mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))

# o3d.visualization.draw_geometries([mesh],
#                                   zoom=0.664,
#                                   front=[-0.4761, -0.4698, -0.7434],
#                                   lookat=[1.8900, 3.2596, 0.9284],
#                                   up=[0.2304, -0.8825, 0.4101],
#                                   )

