import numpy as np
import random

def read_instance(filename):

    with open(filename, 'r') as f:
        text = f.read()

    start = text.find("[[")
    end = text.rfind("]]") + 2

    matrix_str = text[start:end].replace(";", "")

    d = np.array(eval(matrix_str))

    return d
