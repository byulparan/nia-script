#!/usr/bin/env python

import os
import re
import unicodedata

r = re.compile('r-[0-9]+-[0-9]+-[0-9]+-[0-9]+-[가-힣]+\\.\\w+')

for file in os.listdir():
    if not r.search(unicodedata.normalize('NFC',file)):
        print(file)
