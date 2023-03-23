import os
from tqdm import tqdm

os.chdir(directory_name)

counter = 0
for f in tqdm(os.listdir()):
    counter += 1
    if 'Other' not in f:
      if 'session' in f:

        file_name, file_ext = os.path.splitext(f)
        file_title, f_name = file_name.split('session')

        if f_name.startswith('_') or f_name.startswith(' _'):
          f_name = f_name.replace('_', '')
        
        f_name =  f_name.strip()
        f_name  = '00' + f_name + file_ext
        new_name = '{}'.format(f_name)
        print(new_name)
        os.rename(f,new_name)
          
      else:
        # if '.mp4' in f:
          # new_name = f.replace('.mp4', '')
        new_name = f + '.mp4'
        print(new_name)      
      os.rename(f,new_name)