#!/usr/bin/env python

import os

for file in os.listdir('.'):
    names = os.path.splitext(file)
    if names[1][1:] == 'wav':
        os.system(f'lame --quiet -b 320 -h {file} {names[0]}.mp3')
        print(f'{file} converted to mp3')
    
