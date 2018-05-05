from glob import glob
from os import rename
from os import path
import re


for index, fname in enumerate(glob('*.pdf')):
    root, ext = path.splitext(fname)
    root = re.split('-', root)
    root = root[1].replace('_', ' ')
    rename(fname, root.lower() + ext)