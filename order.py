import os
from conversion import * 
from utils import *
import random
import numpy as np
from scipy.spatial.transform import Rotation as R

files_list = []
def find_obj_files(folder_path):
    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        
        if os.path.isfile(full_path) and entry.endswith('.obj') and full_path not in files_list:
            print(full_path)
            files_list.append(full_path)
            v,f = extrac_from_obj(full_path)
            vil, fil = triangle_order(v,f)
            vil, fil = order_obj(vil,fil)
            save_obj(vil, fil, full_path)
        elif os.path.isdir(full_path):
            find_obj_files(full_path)  

folder_path = './datasets'
find_obj_files(folder_path)