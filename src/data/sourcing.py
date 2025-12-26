from  kagglehub import datasets
import os
from pathlib import Path
import sys

try:
    PROJECT_ROOT = Path(__file__).parent.parent
except NameError:
    PROJECT_ROOT = Path(os.getcwd())

GLOBAL_ROOT =  Path(__file__).parent.parent.parent


# Add project root to path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from config import read_yaml


def download_data()-> None: # run this code once to download
    df_path = datasets.dataset_download("sripaadsrinivasan/audio-mnist")
    print(df_path)
    return

def load_set(GLOBAL_ROOT):
    df_paths = read_yaml(GLOBAL_ROOT)
    df_path = df_paths["DATA_PATH"]
    dir_list = []
    for root, dirs, files in os.walk(df_path):
        if len(dirs) != 0:
            #print(dirs)
            for idx in dirs:
                fp = os.path.join(str(df_path), str(idx))
                dir_list.append(fp)
    return dir_list

def sort_files(dir_list):
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    arrs = [zero, one, two, three, four, five, six, seven, eight, nine]
    arr_dict = {0:zero, 1:one, 2:two, 3:three,4:four,5:five,6:six,7:seven,8:eight,9:nine}
    file_to_dir = {}  # Maps (digit, filename) -> directory path
    for idx in dir_list:
        for root, dir, files in os.walk(idx):
            for file in files:
                try:
                    num = int(file[0])
                    if 0 <= num <= 9:
                        arrs[num].append(file)
                        file_to_dir[(num, file)] = idx
                except (ValueError, IndexError):
                    # Skip files that don't start with a digit 0-9
                    continue

    return arr_dict, file_to_dir

# save directories sorted one -> 
