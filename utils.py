import random
import numpy as np
from scipy.spatial.transform import Rotation as R


def save_obj(v,f,file_name):

    with open(file_name, 'w') as f_dest:
        

        text = '####\n# Vertices: ' + str(len(v)) + '\n# Faces: ' + str(len(f)) + '\n#\n####\n'
        f_dest.writelines(text)
        for line in v:
            text = "v " + str(line[0]) + " " + str(line[1]) + " " + str(line[2])+"\n"
            f_dest.writelines(text)
        text = "# " + str(len(v)) + " vertices, 0 vertices normals\n\n"
        f_dest.writelines(text)
        for line in f:
            text = "f " + str(line[0]) + " " + str(line[1]) + " " + str(line[2])+"\n"
            f_dest.writelines(text)
        text = "# " + str(len(f)) + " faces, 0 coords texture\n"
        f_dest.writelines(text)
        text = "\n# End of File"
        f_dest.writelines(text)

def extrac_from_obj(file_name):

    v = []
    f = []
    with open(file_name, 'r') as file:
        righe = file.readlines()
        for i, riga in enumerate(righe):
            riga = riga.split()
            if(len(riga) == 0): continue
            if (riga[0] == "v"):
                v.append([float(riga[1]), float(riga[2]), float(riga[3])])
            elif(riga[0] == "f"):
                f.append([int(riga[1]), int(riga[2]), int(riga[3])])

    return v, f

def triangle_order(v,f):
    new_f = []
    f_dim = len(f)
    for i in range(f_dim):
        s_f = 0
        #v_index = 0
        v0 = float('inf')
        #v1 = float('inf')
        #v2 = float('inf')

        for j, fi in enumerate(f):

            for fii in fi:
                if(v[fii - 1][0]<v0):
                    v0 = v[fii - 1][0]
                    s_f = j

        new_f.append(f[s_f])
        f.pop(s_f)
    return v, new_f

def order_obj(v,f):

    for i,vi in enumerate(v):
        v[i] = (vi,i +1 )

    new_v = []
    new_f = []
    for i, fi in enumerate(f):
        e = []
        for j, fii in enumerate(fi):
            e.append(fii)    
        new_f.append(e)
    for vertex in range(len(v)):
        s_v = v[0]
        v_index = 0
        v0 = float('inf')
        v1 = float('inf')
        v2 = float('inf')

        for new_vert in range(len(v) - vertex):

            if(v[new_vert][0][0]<v0):
                v0 = v[new_vert][0][0]
                s_v = v[new_vert]
                v_index = new_vert

        new_v.append(s_v[0])
        old_index = v[v_index][1]
        v.pop(v_index)

        for i, fi in enumerate(f):
            for j, sc in enumerate(fi):
                if(sc == old_index):
                    new_f[i][j] = vertex + 1
        
    return new_v, new_f

def vertex_augmentation(v,f, rand_t = 1):

    counter = 1
    v_dim = len(v)
    f_dim = len(f)
    f_new = []
    for i in range(f_dim):
        rand = random.random()
        fi = f[i]
        if (rand > rand_t):
            f_new.append(fi)
            continue
        vertex_1 = v[int(fi[0])-1]
        vertex_2 = v[int(fi[1])-1]
        vertex_3 = v[int(fi[2])-1]
        new_x = (vertex_1[0] + vertex_2[0] + vertex_3[0])/3
        new_y = (vertex_1[1] + vertex_2[1] + vertex_3[1])/3
        new_z = (vertex_1[2] + vertex_2[2] + vertex_3[2])/3
        new_vertex = [new_x, new_y, new_z]
        v.append(new_vertex)
        f_new.append([v_dim + counter, fi[1], fi[2]])
        f_new.append([v_dim + counter, fi[0], fi[2]])
        f_new.append([v_dim + counter, fi[1], fi[0]])
        counter +=1
    return v,f_new

def vertex_randomization(v,f, rand_t = 1, alpha = 0.01):

    v_dim = len(v)
    for i in range(v_dim):
        rand = random.random()
        if (rand > rand_t):
            continue

        v[i][0]+=random.uniform(-alpha, alpha)
        v[i][1]+=random.uniform(-alpha, alpha)
        v[i][2]+=random.uniform(-alpha, alpha)

    return v,f

def rotation(v,f, alpha, beta, gamma):

    v_dim = len(v)
    for i in range(v_dim):

        vi = v[i]
        angles = [alpha, beta, gamma]
        rotation = R.from_euler('xyz', angles, degrees=True)
        v[i] = rotation.apply(vi).tolist()
    return v,f
