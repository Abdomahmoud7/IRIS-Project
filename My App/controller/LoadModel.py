import pickle

def LoadModel(file_path : str):
    with open(file_path, 'rb') as file:
        Loaded_model = pickle.load(file)

    return Loaded_model