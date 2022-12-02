  
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

## Features 

### Translation 

Translation is implemented in the matutils section of the code. The translation matrix is give, and is referred to in jungle-scene.py as position. It has been used to position all of the objects, and you can manually use it by using 'w' and 's' to move the baby elephant forwards and backwards. 

### Rotation 

Rotation is implemented in the matutils section of the code. The rotation matrix is given, and is referred to in jungle-scene.py as orientation. It has been used on several of the trees, and you can manually use it on the frog by using 'a' and 'd' to rotate it anticlockwise and clockwise. 

### Local Illumination 

The main light source for this scene is the sun. Local illumination has been programmed using Phong shading. Phong describes how surfaces reflect light by combinging the roughness and shininess of surfaces, which are called diffuse reflection and specular reflection respectively. In the fragment_shader file, vectors are calculated for the shading, as are the light components and the attenuation function. These components are all combined to create the shader, using the normals to calculate the reference points. The normals are perpendicular (at a right angle) to each of the triangles that make up a mesh to show where light reflects best. This gives the shadows, reflections and shading as seen in the jungle scene. 

### Texture Mapping 

Texture mapping is the process of wrapping a 2D texture around a 3D object so it looks detailed and complex. This is used on all the objects in the code, including the skybox. Textures are defined in the textures folder. and are linked to objects using the .mtl file. In material.py, the details from the .mtl file are taken, and in texture.py, the ImageWrapper loads the tecture from the image file. The Texture class below then handles loading the textures and mapping them onto objects, by binding them with wrap parameters and shadow comparisons. This enables the textures to be wrapped as shown in the scene display. 

### Environment Mapping 

Environment mapping maps the distant envrionment as a texture. This includes the skybox, but more focus is on the pool, as pools are reflective. The pool reflects its environment, slightly distored due to the shape of the object. Simple calculations are done to find the light angles for this, to get a projection matrix. This envrionment map created is used on the pool just as a texture would be, and the scene is shown in the water too. 

## Explanation Video

A link to a video recording explaining the code can be found here: 

## Authors 

- Kate Frances Belson (Undergraduate Student studying BSc Computer Science at the University of Exeter)

## Handle

https://github.com/kfb19/graphics-coursework

## Publish Date 

- Version 0.0.1 was published on 02/12/2022
