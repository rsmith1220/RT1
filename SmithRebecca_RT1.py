from gl import Raytracer, V3
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

eyes = Material(diffuse = (0, 0, 0))
snow = Material(diffuse = (1, 1, 1))
eyes1 = Material(diffuse = (0, 0, 0.2))



rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (-1,-1,-1) ))

#cuerpo
rtx.scene.append( Sphere(V3(0,2.5,-10), 1, snow))
rtx.scene.append( Sphere(V3(0,0.5,-10), 1.3, snow))
rtx.scene.append( Sphere(V3(0,-2.3,-10), 1.7, snow))

#ojos
rtx.scene.append( Sphere(V3(0.3,1.4,-5), 0.08, eyes))
rtx.scene.append( Sphere(V3(-0.3,1.4,-5), 0.08, eyes))

rtx.scene.append( Sphere(V3(0.3,1.4,-7), 0.1, eyes1))
rtx.scene.append( Sphere(V3(-0.3,1.4,-7), 0.1, eyes1))


rtx.glRender()

rtx.glFinish("output.bmp")