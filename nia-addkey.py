#!/Users/byul/.pyenv/shims/python

import os

key = input('add key: ')

for file in os.listdir():
    name = key + '-' + file
    os.rename(file, name)
    
