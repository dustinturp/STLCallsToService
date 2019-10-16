
import os
import glob
import numpy as np
import pandas as pd
os.chdir(os.getcwd())

# Combine csv files in directory to a single file
extension = 'csv' #CSV for windows
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv specify encoding
FileName = input("Enter File Name ")
combined_csv.to_csv( FileName, index=False, encoding='utf-8-sig')
