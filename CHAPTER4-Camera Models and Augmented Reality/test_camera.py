import camera
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from scipy import ndimage

points = np.loadtxt('./3D-house/house.p3d').T
points = np.vstack((points,np.ones(points.shape[1])))

# setup camera
P = np.hstack((np.eye(3), np.array([[0], [0], [-10]])))
cam = camera.Camera(P)
x = cam.project(points)

# plot project
plt.figure()
plt.plot(x[0],x[1],'k.')

# create transformation
r = 0.05*np.random.rand(3)
rot = camera.rotation_matrix(r)
# rotate camera and project
plt.figure()
for t in range(20):
    cam.P = np.dot(cam.P,rot)
    x = cam.project(points)
    plt.plot(x[0],x[1],'k.')

K = np.array([[1000,0,500],[0,1000,300],[0,0,1]])
tmp = camera.rotation_matrix([0,0,1])[:3,:3]
Rt = np.hstack((tmp,np.array([[50],[40],[30]])))
cam = camera.Camera(np.dot(K,Rt))
print (K,Rt)
print (cam.factor())

plt.show()
