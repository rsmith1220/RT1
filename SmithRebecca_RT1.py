from gl import Raytracer, V3
from figures import *
from lights import *


width = 1024
height = 1024

# Materiales

eyes = Material(diffuse = (0, 0, 0))
snow = Material(diffuse = (1, 1, 1))
eyes1 = Material(diffuse = (0.682, 0.776, 0.812))
nose = Material(diffuse = (1, 0.647, 0))
rocks=Material(diffuse=(0.4,0.4,0.4))



rtx = Raytracer(width, height)

rtx.lights.append( AmbientLight( ))
rtx.lights.append( DirectionalLight(direction = (1,-1,-1) ))

#cuerpo
rtx.scene.append( Sphere(V3(0,2.5,-10), 1, snow))
rtx.scene.append( Sphere(V3(0,0.5,-10), 1.3, snow))
rtx.scene.append( Sphere(V3(0,-2.3,-10), 1.7, snow))

#ojos
rtx.scene.append( Sphere(V3(0.3,1.4,-5), 0.08, eyes))
rtx.scene.append( Sphere(V3(-0.3,1.4,-5), 0.08, eyes))

rtx.scene.append( Sphere(V3(0.4,2,-7), 0.2, eyes1))
rtx.scene.append( Sphere(V3(-0.4,2,-7), 0.2, eyes1))


#nariz
rtx.scene.append( Sphere(V3(0,1.3,-5), 0.08, nose))

#Boca
rtx.scene.append( Sphere(V3(0,1,-5), 0.06, eyes))
rtx.scene.append( Sphere(V3(0.3,1.1,-5), 0.06, eyes))
rtx.scene.append( Sphere(V3(-0.3,1.1,-5), 0.06, eyes))
rtx.scene.append( Sphere(V3(0.2,1,-5), 0.06, eyes))
rtx.scene.append( Sphere(V3(-0.2,1,-5), 0.06, eyes))

#Botones
rtx.scene.append( Sphere(V3(0,0.4,-5), 0.08, rocks))
rtx.scene.append( Sphere(V3(0,-0.3,-5), 0.15,rocks))
rtx.scene.append( Sphere(V3(0,-0.8,-5), 0.2, rocks))

rtx.glRender()

rtx.glFinish("output.bmp")