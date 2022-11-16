#!/usr/bin/env python

import os
from pathlib import Path
import soundfile as sf
import sys

# 파일명 앞에 fs-붙임
for file in os.listdir():
    if os.path.splitext(file)[1][1:] == 'wav':
        name = 'fs-' + file
        os.rename(file, name)
    
# trim 폴더 생성
if not Path('trim').is_dir():
    os.mkdir('trim')

# 트림
filelen = 45

def get_filelen(file):
    f = sf.SoundFile(file)
    return f.frames / f.samplerate

for file in os.listdir('.'):
    if os.path.splitext(file)[1][1:] == 'wav':
        command = False
        if len(sys.argv) != 2:
            command = f'ffmpeg -v quiet -ss 0 -i {file} -t {filelen} -af afade=in:st=0:d=0.1,afade=out:st={filelen - 0.1}:d=0.1 -c:a pcm_s24le  trim/{file} '
        else:
            command = f'ffmpeg -v quiet -ss {get_filelen(file) - filelen} -i {file} -t {filelen} -af afade=in:st=0:d=0.1,afade=out:st={filelen - 0.1}:d=0.1 -c:a pcm_s24le  trim/{file} '
        os.system(command)
        print(f'{file} trim')
        os.remove(file)
        os.rename(f'trim/{file}', file)

os.rmdir('trim')

#노멀라이즈
if not Path('normal').is_dir():
    os.mkdir('normal')

for file in os.listdir():
    if os.path.splitext(file)[1][1:] == 'wav':
        # os.system(f'ffmpeg-normalize {file}  -t -21 -f -o {file}')
        os.system(f'ffmpeg -v quiet -i {file} -af loudnorm=I=-21:TP=-2:LRA=11 -c:a pcm_s24le -ar 96000  normal/{file}  ')
        print(f'{file} normalized')
        os.remove(file)
        os.rename(f'normal/{file}', file)

os.rmdir('normal')
