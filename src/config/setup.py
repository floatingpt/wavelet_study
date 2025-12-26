from pathlib import Path
import os
import yaml

try:
    GLOBAL_ROOT = Path(__file__).parent.parent.parent
except NameError:
    GLOBAL_ROOT = Path(os.getcwd())



def read_yaml(GLOBAL_ROOT):
    paths_file = GLOBAL_ROOT / "paths.yaml"
    with open (paths_file, 'r') as infile:
        config = yaml.safe_load(infile)
        DATA_PATH = Path(config['data_path'])
        PATHS = {"DATA_PATH": DATA_PATH}
    return PATHS