import os
from pathlib import Path
import sys
import argparse
try:
    PROJECT_ROOT = Path(__file__).parent.parent
except NameError:

    PROJECT_ROOT = Path(os.getcwd())

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.data import wav_to_matr_arr
from src.visualization import plot_series


def main():
    parse = argparse.ArgumentParser(description="Wavelet Scattering Transform Classification")
    parse.add_argument('--subset', default=None)
    



    print("DATA PREPROCESSING")
    print("=" * 100)

    matrices = wav_to_matr_arr(PROJECT_ROOT)
    #plot_series(matrices, PROJECT_ROOT) 
    "uncomment to visualize time series"

    print("=" * 100)
    print("PROCESSING COMPLETE")
