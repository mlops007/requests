import os
from tqdm import tqdm
import pandas as pd

print(os.getcwd())
os.chdir('C:\\Users\\AnkanDatta\\Desktop\\Fundamentals Exam - Admin Excel')
print(os.getcwd())

for f in tqdm(os.listdir()):
    print(f)
    file_name, file_ext = os.path.splitext(f)
    print(file_name, '\t', file_ext)
    if file_ext == '.xlsx':
      new_ext = '.csv'
      f_name  = '00' + file_name + new_ext
      new_name = '{}'.format(f_name)
      print(new_name)
      os.rename(f,new_name)