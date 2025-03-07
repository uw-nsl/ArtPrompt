import json
import datasets
from tqdm.auto import tqdm

def data_aug(data, aug=False):
    if aug:
        if " " in data:
            for c in "·~*`":
                if c not in data:
                    return data.replace(" ", c)
                

    
    return data     


def parse(dataset_file):
    '''
    parsing dataset file
    '''
    return dataset_file

def load_dataset(task, ft=None):
    if task == "s":
        file_path = "dataset/ViTC/vitc-s.json"
    elif task == "l":
        file_path = "dataset/ViTC/vitc-l.json"
    else:
        raise ValueError("task should be s, l")
    
    
    with open(file_path, "r") as f:
        dataset = json.load(f)

    number_dataset = len(dataset)

    
    return parse(dataset)