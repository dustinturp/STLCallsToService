
import os
import glob
import pandas as pd

path = os.getcwd()
# Combine csv files in directory to a single file
extension = 'csv'
all_filenames = glob.glob(os.path.join(path, "*.csv"))

print("number of files loaded in to data frame: ", len(all_filenames))
# for file in all_filenames:
#     df = pd.read_csv(file, sep=',', encoding='utf-8')
df = pd.concat([pd.read_csv(f, sep=',', encoding='utf-8') for f in all_filenames])

# print(df.head())
# Summary of data loaded
print("Total Records in Data Frame. ", len(df.index))

# count for each unique month

print("Count of each month... ", df.groupby('CodedMonth').size())

# count of unique types of crime


#export to csv specify encoding
FileName = input("Enter File Name ")
# status writing file
print("writing file to csv...")
df.to_csv( FileName, index=True, encoding='utf-8-sig')

# all clear 
print("all done...")