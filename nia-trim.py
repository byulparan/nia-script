#!/usr/bin/env python

import os
from pathlib import Path
import re
import unicodedata
import soundfile as sf
import sys

if not Path('trim').is_dir():
    os.mkdir('trim')

r = re.compile('합성')

if re.compile('합성').search(unicodedata.normalize('NFC',  os.getcwd())):
    filelen = 45
else:
    filelen = 100

def get_filelen(file):
    f = sf.SoundFile(file)
    return f.frames / f.samplerate


for file in os.listdir('.'):
    if os.path.splitext(file)[1][1:] == 'wav':
        if len(sys.argv) != 2:
            os.system(f'ffmpeg -v quiet -ss 0 -i {file} -t {filelen} -af afade=in:st=0:d=0.1,afade=out:st={filelen - 0.1}:d=0.1 -c:a pcm_s24le  trim/{file} ')
            print(f'{file} trimed')
        else:
            start = get_filelen(file) - filelen
            os.system(f'ffmpeg -v quiet -ss {start} -i {file} -t {filelen} -af afade=in:st=0:d=0.1,afade=out:st={filelen - 0.1}:d=0.1 -c:a pcm_s24le  trim/{file} ')
            print(f'{file} trimed')
        os.remove(file)
        os.rename(f'trim/{file}', file)

os.rmdir('trim')



