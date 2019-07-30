import os
import glob
import pandas as pd

# Grab all csv file names in the current directory
extension = 'csv'
arr_csv = [i for i in glob.glob('*.{}'.format(extension))]

# Concatenate the csvs in the list, in reversed order
concat_csv = pd.concat([pd.read_csv(i) for i in arr_csv[::-1]])

# Export to csv
concat_csv.to_csv("output.csv", index=False, encoding='utf-8')
