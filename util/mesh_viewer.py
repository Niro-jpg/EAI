import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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

    
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser("view meshes")
    parser.add_argument('--files', nargs='+', default=['datasets\shrec_16\ok\test\handsOK5_orientation1_vertex0_randomized0.obj'], type=str,
                        help="list of 1 or more .obj files")
    args = parser.parse_args()

    miao = args.files
    vertices, faces = extrac_from_obj(miao[0])
    for i, face in enumerate(faces):
        for j, fi in enumerate(face):
            faces[i][j] -= 1
    vertices = np.array(vertices)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Crea la mesh 3D
    ax.add_collection3d(Poly3DCollection([vertices[face] for face in faces], 
                                        facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Imposta limiti degli assi
    ax.set_xlim([min(vertices[:, 0]), max(vertices[:, 0])])
    ax.set_ylim([min(vertices[:, 1]), max(vertices[:, 1])])
    ax.set_zlim([min(vertices[:, 2]), max(vertices[:, 2])])

    # Mostra il grafico
    plt.show()



