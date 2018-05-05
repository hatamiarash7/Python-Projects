from glob import glob
from os import rename
for index, fname in enumerate(glob('*.mp4')):
    rename(fname, str(index + 1) + '.mp4')