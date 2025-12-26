import numpy as np
import librosa
from pathlib import Path
import os

try:
    PROJECT_ROOT = Path(__file__).parent.parent
    GLOBAL_ROOT = Path(__file__).parent.parent.parent
except NameError:
    PROJECT_ROOT = Path(os.getcwd())
    GLOBAL_ROOT = Path(os.getcwd()).parent

from .sourcing import sort_files, load_set 



def wav_to_matr_arr(GLOBAL_ROOT):

    # Initialize lists for each digit (0-9)
    matrices = [[] for _ in range(10)]

    dir_list = load_set(GLOBAL_ROOT)
    arr_dict, file_to_dir = sort_files(dir_list)
    run = 0
    for key in arr_dict.keys(): # get keys for 0->9 indexing file arrays
        for file in arr_dict[key]: # access .wav file values
            # Get the correct directory for this file
            source_dir = file_to_dir.get((key, file))
            if source_dir is None:
                print(f"WARNING: No source directory found for {file}")
                continue
                
            try:
                name = os.path.join(str(source_dir), str(file)) # concatenate to get file name
                if not os.path.exists(name):
                    print(f"ERROR: File does not exist: {name}")
                    continue
                wav, sr = librosa.load(name) # wav file and sampling rate
                matrices[key].append(wav) # append loaded wav files to list
                run +=1
                if run % 100 == 0:  # modulo
                    rund = run // 100  # floor division
                    print(f"{rund * 100} Files Loaded" )

            except Exception as e:
                print(f"ERROR loading {file}: {type(e).__name__}: {e}")
                print(f"{file} unresponsive, continuing.")
    
    # Convert lists to numpy arrays and pad to homogeneous size
    padded_matrices = []
    
    # Find the maximum length across all audio arrays
    max_length = 0
    for digit_arrays in matrices:
        for audio_array in digit_arrays:
            if len(audio_array) > max_length:
                max_length = len(audio_array)
    
    # Pad each array to the maximum length
    for digit_arrays in matrices:
        padded_digit_arrays = []
        for audio_array in digit_arrays:
            if len(audio_array) < max_length:
                # Pad with zeros at the end
                padded = np.pad(audio_array, (0, max_length - len(audio_array)), mode='constant', constant_values=0)
            else:
                padded = audio_array
            padded_digit_arrays.append(padded)
        padded_matrices.append(np.array(padded_digit_arrays))
    
    return padded_matrices