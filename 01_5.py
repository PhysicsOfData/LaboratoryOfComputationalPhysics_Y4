from numpy import pi

densities = {"Al":[0.5,1,2],"Fe":[3,4,5],"Pb": [15,20,30]}
radii = [1,2,3]

linear=[densities[i][0] for i in densities] #list of the linear density of Al,Fe,Pb
superficial=[densities[i][1] for i in densities] #list of superficila density
volumetric=[densities[i][2] for i in densities] #list of volumetric density

Alcircle=[(linear[0],j) for j in radii] #list of tuples (linear density,radius)
Fecircle=[(linear[1],j) for j in radii]
Pbcircle=[(linear[2],j) for j in radii]

Aldisk=[(superficial[0],j) for j in radii] #list of tuples (sup density,radius)
Fedisk=[(superficial[0],j) for j in radii]
Pbdisk=[(superficial[0],j) for j in radii]

Alsphere=[(volumetric[0],j) for j in radii] #list of tuples (sup density,radius)
Fesphere=[(volumetric[0],j) for j in radii]
Pbsphere=[(volumetric[0],j) for j in radii]

fun=[lambda r: 2*pi*r, lambda r: pi* r**2 , lambda r: 4/3 * pi* r**3]

def pesocerchio(dl,r):
    return dl * fun[0](r)
def pesodisco(ds,r):
    return ds * fun[1](r)
def pesodisco(dv,r):
    return dv * fun[2](r)

for i in Alcircle:
    print("Weight of Al circle with radius %d is %f" % (i[1],pesocerchio(i[0],i[1])))
