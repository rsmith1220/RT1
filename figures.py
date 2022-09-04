import numpy as np
import matesRS

WHITE = (1,1,1)
BLACK = (0,0,0)

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObj):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObj = sceneObj

class Material(object):
    def __init__(self, diffuse = WHITE):
        self.diffuse = diffuse


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        L = matesRS.subtract(self.center, orig)#lista
        tca = matesRS.dot(L, dir)#numero

        d = (np.linalg.norm(L) ** 2 - tca ** 2) ** 0.5
        # print(d)

        # lnormal=matesRS.normal(L)

        # lcuadro=[]
        # for i in lnormal:
        #     a=i**2
        #     lcuadro.append(a)

        # tcacuadro=tca**2

        # ltca=[]
        # for i in lcuadro:
        #     a=i-tcacuadro
        #     ltca.append(a)
        # print(ltca )

        # dd=[]
        # for i in ltca:
        #     a=i**0.5
        #     dd.append(a)
            


        # d = (ltca) ** 0.5

        if d > self.radius:
            return None

        thc = (self.radius ** 2 - d ** 2) ** 0.5

        t0 = tca - thc
        t1 = tca + thc

        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = O + t0 * D
        todir = []
        for i in dir:
            float(i)
            a=i*t0
            todir.append(a)


        P = matesRS.add(orig, todir)
        normal = matesRS.subtract(P, self.center)
        normal = matesRS.normal(normal)

        return Intersect(distance = t0,
                         point = P,
                         normal = normal,
                         sceneObj = self)
