#!/usr/bin/env python

import os
from pathlib import Path


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
