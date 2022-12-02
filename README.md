  
# 3D Graphics Jungle Scene

## Introduction

This Python program renders a 3D jungle scene, with the use of [OpenGL](https://pypi.org/project/PyOpenGL/ "OpenGL") and [PyGame](https://www.pygame.org/news "PyGame"). 

## Prerequisites

- [Python 3.10.7](https://www.python.org/downloads/ "Python 3.10.7")
- [OpenGL](https://pypi.org/project/PyOpenGL/ "OpenGL") 
- [PyGame](https://www.pygame.org/news "PyGame")
- [NumPy](https://numpy.org/ "NumPy")
- An IDE such as VS Code if you wish to view or edit code 

## Getting Started 

Use command line to switch to the correct directory containing all the files. Then run the following Python command to run the scene. 

```bash
python jungle-main.py
```

## Need-to-know Commands 

There are several commands you can use in the code: 
- 

## Developer Documentation
Files: 
1. models - contains the .obj and .mtl files for all object models used in the scene. 
	- .obj files - these contain the lists of vertices needed to build the models. 
	- .mtl files - these contain the details needed to texture map textures onto the objects. 
2. shaders - contains the code for the shaders used in the program, such as phong, environment and shadow mapping. 
3. textures - contains the textures to be mapped onto models and the skybox. 
4. BaseModel.py - base class of all models, which implements the basic draw function for traingular meshes. 
5. blender.py - used to read models from blender. 
6. camera.py - handles the camera by defining it and the starting viewpoint using the azimuth and zenith angles, as well as the distance of the camera to the centre point. 
7. cubeMap.py - code for handling a cube map texture. 
8. environmentMapping.py - code for environment mapping (mapping the environment onto one object). 
9. framebuffer.py - defines the framebuffer, which contains the display. 
10. jungle-main.py - imports the models/objects, defines their transformations, and sets up the scene. 
11. lightSource.py - adds a main light source to the scene - the sun, in this case. 
12. material.py - a class to hold details of materials (from .mtl files) for rendering. 
13. matutils.py - defines the matrices for translation, rotation and scaling. 
14. mesh.py - calculates the meshes of the models/objects by linking their vertices into lines. 
15. scene.py - draws the jungle scene by setting modelss, shaders, the camera, the light source etc, as well as defining physical commands to move the scene. 
16. shaders.py -loads and compiles the shaders from the shaders folder. 
17. ShadowMapping.py - uses a Phong shader to calculate the shadows for objects, in relation to their textures and the light source. 
18. showTexture.py - renders a flattened cube to help with debugging the code. 
19. skyBox.py - builds the skybox which gives depth and a background to the scene, using a cube mesh. 
20. texture.py - handles texture loading for texture mapping, from the file to wrapping it around the object and binding it, finally loading the texture in the buffer. 
21. sphereModel.py - implements code for a sphere for the light source. 


## Literature Review and Testing

A link to a video recording explaining the code can be found here: 

## Authors 

- Kate Frances Belson (Undergraduate Student studying BSc Computer Science at the University of Exeter)

## Handle

https://github.com/kfb19/graphics-coursework

## Publish Date 

- Version 0.0.1 was published on 02/12/2022
