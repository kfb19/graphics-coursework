import pygame

# import the scene class
from cubeMap import FlattenCubeMap
from scene import Scene

from lightSource import LightSource

from blender import load_obj_file

from BaseModel import DrawModelFromMesh

from shaders import *

from ShadowMapping import *

import random

from sphereModel import Sphere

from skyBox import *

from environmentMapping import *

class ExeterScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.light = LightSource(self, position=[3., 4., -3.])

        self.shaders='phong'

        # for shadow map rendering
        self.shadows = ShadowMap(light=self.light)
        self.show_shadow_map = ShowTexture(self, self.shadows)

        #bamboo random generation 

        self.bamboos = []

        for counter in range(10):
            angle = random.randint(0, 360)
            bamboo = load_obj_file('models/bamboo.obj')
            bamboo = [DrawModelFromMesh(scene=self, M=poseMatrix(position=[(counter-5), -7, -4], scale=0.015, orientation=angle), mesh=mesh, shader=self.shaders, name='bamboo') for mesh in bamboo]
            self.bamboos.append(bamboo)

        for counter in range(6):
            angle = random.randint(0, 360)
            bamboo = load_obj_file('models/bamboo.obj')
            bamboo = [DrawModelFromMesh(scene=self, M=poseMatrix(position=[(counter-5), -7, -3], scale=0.015, orientation=angle), mesh=mesh, shader=self.shaders, name='bamboo') for mesh in bamboo]
            self.bamboos.append(bamboo)  

        self.leafyplants = []
        xpos = -5
        zpos = 0

        for i in range(5):
            for j in range(4):
                leafyplant = load_obj_file('models/leafyplant.obj') 
                leafyplant = [DrawModelFromMesh(scene=self, M=poseMatrix(position=[xpos,-5.8,zpos], scale=0.2), mesh=mesh, shader=self.shaders, name='leafyplant') for mesh in leafyplant]
                self.leafyplants.append(leafyplant)
                zpos += 2.5
            xpos += 1
            zpos = 0

        rock = load_obj_file('models/rock.obj')
        self.rock = [DrawModelFromMesh(scene=self, M=poseMatrix(position=[4,-6,3], scale=0.015), mesh=mesh, shader=self.shaders, name='rock') for mesh in rock]

        frog = load_obj_file('models/frog.obj')
        self.frog = [DrawModelFromMesh(scene=self, M=poseMatrix(position=[4.5,-5,3], scale=5), mesh=mesh, shader=self.shaders, name='frog') for mesh in frog]
     
        elephant = load_obj_file('models/elephant.obj')
        self.elephant = DrawModelFromMesh(scene=self, M=poseMatrix(position=[2.5,-4,2], scale=0.5), mesh=elephant[0], shader=PhongShader())

        babyelephant = load_obj_file('models/elephant.obj')
        self.babyelephant = DrawModelFromMesh(scene=self, M=poseMatrix(position=[3.5,-4,2.5], scale=0.3), mesh=babyelephant[0], shader=PhongShader())

        # draw a skybox for the horizon
        self.skybox = SkyBox(scene=self)

        self.show_light = DrawModelFromMesh(scene=self, M=poseMatrix(position=self.light.position, scale=0.2), mesh=Sphere(material=Material(Ka=[10,10,10])), shader=PhongShader())

        self.environment = EnvironmentMappingTexture(width=400, height=400)

        pool = load_obj_file('models/pool.obj')    
        self.pool = DrawModelFromMesh(scene=self, M=translationMatrix([4,-6,4]), mesh=pool[0], shader=EnvironmentShader(map=self.environment), name='pool') 

        floor = load_obj_file('models/floor.obj')
        self.floor = DrawModelFromMesh(scene=self, M=translationMatrix([0,-7,0]), mesh=floor[0], shader=self.shaders, name='floor') 
        # this object allows to visualise the flattened cube
        self.flattened_cube = FlattenCubeMap(scene=self, cube=self.environment)
        self.show_texture = ShowTexture(self, Texture('obj_textures/mossy-ground.jpg'))


    def draw_shadow_map(self):
        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # also all models from the bamboo
        for bamboo in self.bamboos:
            for model in bamboo:
                model.draw()


        for leafyplant in self.leafyplants:
            for model in leafyplant:
                model.draw()


        self.elephant.draw()
        self.babyelephant.draw()
        for model in self.rock:
                model.draw()

        for model in self.frog:
                model.draw()

        model.draw()

    def draw_reflections(self):
        self.skybox.draw()

        for model in self.models:
            model.draw()

        # also all models from the bamboo
        for bamboo in self.bamboos:
            for model in bamboo:
                model.draw()

        for leafyplant in self.leafyplants:
            for model in leafyplant:
                model.draw()
        
        for model in self.rock:
                model.draw()

        for model in self.frog:
                model.draw()

        self.elephant.draw()
        self.babyelephant.draw()
        model.draw()


    def draw(self, framebuffer=False):
        '''
        Draw all models in the scene
        :return: None
        '''

        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # when using a framebuffer, we do not update the camera to allow for arbitrary viewpoint.
        if not framebuffer:
            self.camera.update()

        # first, we draw the skybox
        self.skybox.draw()

        # render the shadows
        self.shadows.render(self)

        # when rendering the framebuffer we ignore the reflective object
        if not framebuffer:
            #glEnable(GL_BLEND)
            #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#            self.envbox.draw()
            #self.environment.update(self)
            #self.envbox.draw()

            self.environment.update(self)


            self.elephant.draw()
            self.babyelephant.draw()
            for model in self.rock:
                model.draw()

            for model in self.frog:
                model.draw()

            for leafyplant in self.leafyplants:
                for model in leafyplant:
                    model.draw()

            self.floor.draw()
            self.pool.draw()
            #self.sphere.draw()
            #glDisable(GL_BLEND)

            # if enabled, show flattened cube
            self.flattened_cube.draw()

            # if enabled, show texture
            self.show_texture.draw()

            self.show_shadow_map.draw()

        # then we loop over all models in the list and draw them
        for model in self.models:
            model.draw()

        # also all models from the bamboo
        for bamboo in self.bamboos:
            for model in bamboo:
                model.draw()

        for leafyplant in self.leafyplants:
            for model in leafyplant:
                model.draw()

        self.elephant.draw()
        self.babyelephant.draw()
        for model in self.rock:
                model.draw()

        for model in self.frog:
                model.draw()

        self.show_light.draw()

        # once we are done drawing, we display the scene
        # Note that here we use double buffering to avoid artefacts:
        # we draw on a different buffer than the one we display,
        # and flip the two buffers once we are done drawing.
        if not framebuffer:
            pygame.display.flip()

    def keyboard(self, event):
        '''
        Process additional keyboard events for this demo.
        '''
        Scene.keyboard(self, event)

        if event.key == pygame.K_c:
            if self.flattened_cube.visible:
                self.flattened_cube.visible = False
            else:
                #print('--> showing cube map')
                self.flattened_cube.visible = True

        if event.key == pygame.K_t:
            if self.show_texture.visible:
                self.show_texture.visible = False
            else:
                #print('--> showing texture map')
                self.show_texture.visible = True

        if event.key == pygame.K_z:
            if self.show_shadow_map.visible:
                self.show_shadow_map.visible = False
            else:
                #print('--> showing shadow map')
                self.show_shadow_map.visible = True

        if event.key == pygame.K_1:
            #print('--> using Flat shading')
            self.elephant.use_textures = True
            self.elephant.bind_shader('flat')
        
        if event.key == pygame.K_a:
            # Rotate elephant anticlockwise
            self.elephant.M = np.matmul(translationMatrix([0,0,0]), rotationMatrixY(-1))
            self.elephant.draw()


        if event.key == pygame.K_d:
            #Rotate elephant clockwise
            self.elephant.M = np.matmul(translationMatrix([0,0,0]), rotationMatrixY(1))
            self.elephant.draw()


        if event.key == pygame.K_w:
            #Move baby elephant forwards
            self.babyelephant.M = np.matmul(translationMatrix([3.5,-4,3.5]), rotationMatrixX(0))
            self.babyelephant.draw()

        if event.key == pygame.K_s:
            #Move baby elephant backwards 
            self.babyelephant.M = np.matmul(translationMatrix([3.5,-4,1.5]), rotationMatrixX(0))
            self.babyelephant.draw()

        if event.key == pygame.K_2:
            #print('--> using Phong shading')
            self.elephant.use_textures = True
            self.elephant.bind_shader('phong')

        elif event.key == pygame.K_4:
            #print('--> using original texture')
            self.elephant.shader.mode = 1

        elif event.key == pygame.K_6:
            self.elephant.mesh.material.alpha += 0.1
            #print('--> elephant alpha={}'.format(self.elephant.mesh.material.alpha))
            if self.elephant.mesh.material.alpha > 1.0:
                self.elephant.mesh.material.alpha = 0.0

        elif event.key == pygame.K_7:
            #print('--> no face culling')
            glDisable(GL_CULL_FACE)

        elif event.key == pygame.K_8:
            #print('--> glCullFace(GL_FRONT)')
            glEnable(GL_CULL_FACE)
            glCullFace(GL_FRONT)

        elif event.key == pygame.K_9:
            #print('--> glCullFace(GL_BACK)')
            glEnable(GL_CULL_FACE)
            glCullFace(GL_BACK)

        elif event.key == pygame.K_BACKQUOTE:
            if glIsEnabled(GL_DEPTH_TEST):
                #print('--> disable GL_DEPTH_TEST')
                glDisable(GL_DEPTH_TEST)
            else:
                #print('--> enable GL_DEPTH_TEST')
                glEnable(GL_DEPTH_TEST)


if __name__ == '__main__':
    # initialises the scene object
    # scene = Scene(shaders='phong')
    scene = ExeterScene()

    # starts drawing the scene
    scene.run()
