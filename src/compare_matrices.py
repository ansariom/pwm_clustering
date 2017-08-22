import numpy as np

def load_matrices(infile):
    mtx_dict = {}
    mtx_file = open(infile)
    for line in iter(mtx_file):
        if (line.startswith(">")):
            pwm_name = line
            mtx_arr = []
            continue
        if(line.startswith("=")):
            line_parts = line.split("\t")
            mtx_arr.append(line_parts)
        else:
            mtx_dict[pwm_name] = mtx_arr
    return mtx_dict

if __name__ == "__main__":
    infile = ""
    load_matrices(infile)