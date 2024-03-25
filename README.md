# PLY to Mesh Generator
You'll be able to convert a point cloud (.ply file) to a mesh (.gltf).


# Project Setup
Follow these steps:

    git clone <repo-url>
    cd Ply-to-mesh-generator
    pip install open3d

This will start the project on your localhost.

# How to Use
Rename your ply file to "pcd.ply".
Place the ply file in the same directory as the converter.py and run the following command in the terminal.
    
    python converter.py

Once the code executes, check the directory again for a "mesh.gltf" file. That you can view blender or Splat-mesh-Viewer. 
