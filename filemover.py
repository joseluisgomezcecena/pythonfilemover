import glob
import os
import shutil

list_of_files = glob.glob('C:/xampp/htdocs/frontend/carapp/app/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

shutil.copy2(latest_file, 'C:/xampp/htdocs/tests/', follow_symlinks = True) 

 
#shutil.copytree(src, dst, symlinks = True) 
#pyinstaller --onefile -w 'filemover.py' to make an exe file