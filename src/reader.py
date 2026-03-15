import numpy as np
import re

def read_instance(file_path):
  
    with open(file_path, 'r') as f:
        content = f.read()

    # On récupère la matrice contenue entre d=[ ... ]
    matrix_str = re.search(r"d=\[(.*)\];", content, re.S).group(1)
    matrix = eval("[" + matrix_str + "]")

    D = np.array(matrix)

    return D
