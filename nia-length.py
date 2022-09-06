#!/usr/bin/env python

import os
from pathlib import Path
import soundfile as sf
import unicodedata
import re
import sys


r = re.compile('합성')

if len(sys.argv) == 2:
    if not( sys.argv[1] == '1' or sys.argv[1] == '2'):
        print('not support operation.')
        sys.exit()
    

for file in Path('.').rglob('*.wav'):
    limit = 45 if r.search( unicodedata.normalize('NFC', file.absolute().as_posix()) ) else 100
    limit = limit * 96000
    f = sf.SoundFile(file)
    if f.frames < limit:
        print(f"{file} is too short(sec: {f.frames/f.samplerate} | samples: {f.frames} < {limit}).")
    else:
        if len(sys.argv) == 2:
            if sys.argv[1] == '1':
                print(f"{f.frames} == {file}" )
            elif sys.argv[1] == '2':
                if f.frames != limit:
                    print(f'{file} is not {limit}')

