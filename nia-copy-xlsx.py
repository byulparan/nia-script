from pathlib import Path
import shutil
import re
import unicodedata


for index, file in enumerate(Path('/Users/byul/Downloads/metadata').iterdir()):
    if file.is_file():
        print(file)
        shutil.copyfile(file,f'/Users/byul/code/neutune/합성/083-버스탑승/fs-2-2-83-{index + 1}-추가.xlsx')
        index += 1

    
