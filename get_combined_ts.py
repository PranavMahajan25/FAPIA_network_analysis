import os
import numpy as np

# all_ts_directory = '../Glasser180ts_run1/'
# output_directory = '../Glasser180ts_run1_npy/'
# num_ts = 180

# all_ts_directory = '../Glasser360ts_run1/'
# output_directory = '../Glasser360ts_run1_npy/'
# num_ts = 360

all_ts_directory = '../AAL116ts_run1/'
output_directory = '../AAL116ts_run1_npy/'
num_ts = 116

len_ts = 260

for folder_name in os.listdir(all_ts_directory):
    if folder_name[:3] == 'sub':       
        subj_folder = os.path.join(all_ts_directory, folder_name)
        ts_mat = np.zeros((num_ts, len_ts))
        for i in range(num_ts):
            ts_filename = 'out_' + str(i+1).zfill(3) + '.txt'
            tmp_ts = np.loadtxt(os.path.join(subj_folder, ts_filename))
            ts_mat[i,:] = tmp_ts
        output_file = os.path.join(output_directory, folder_name+'.npy')
        with open(output_file, 'wb') as f:
            np.save(f, ts_mat)