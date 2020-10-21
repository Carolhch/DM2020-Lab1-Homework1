import glob

def load_file_in_folder(path):
    data = []
    file_list = glob.glob(path + '/*.txt')
    for file_path in file_list:
        f = open(file_path,"r")
        data+=f.read().split('\n')
    data = list(filter(None, data))
    return data

def format_row_from_file(data):
    ## format data for pandas dataframe
    D = []
    for s in data:
        D.append([s])
    return D

def data_split(data, split, index):
    D = []
    for s in data:
        D.append(s.split(split)[index])
    return D
