import matplotlib.pyplot as plt
from pathlib import Path
import os
import sys

try:
    PROJECT_ROOT = Path(__file__).parent.parent
except NameError:
    PROJECT_ROOT = Path(os.getcwd())

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

GLOBAL_ROOT = Path(__file__).parent.parent.parent

from data.sourcing import load_set, sort_files
from data.get_timeseries import wav_to_matr_arr




def plot_series(matrices, GLOBAL_ROOT):
    dir_list = load_set(GLOBAL_ROOT)
    arr_dict, path_dict = sort_files(dir_list)
    matrices = wav_to_matr_arr(GLOBAL_ROOT)
    zero_wav_matr = matrices[0]
    first_wav = zero_wav_matr[0,:]
    plt.plot(first_wav)
    plt.title("Audio Signal")
    plt.xlabel("Time(s)")
    plt.ylabel("Amplitude(dB)")
    plt.show()
