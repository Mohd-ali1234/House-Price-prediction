import json
import pickle

__locations = None
__data_colums = None
__model = None


def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_colums
    global __locations

    with open("./artifacts/columns.json","r") as f:
        __data_colums = json.load(f)["data_columns"]
        __locations = __data_colums[3:]
    with open("./artifacts/banglore_home_price_model.pickle","rb") as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

if __name__== "__main__":
    load_saved_artifacts()
    print(get_location_names())