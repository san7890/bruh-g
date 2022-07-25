import glob
import os
import shutil

os.chdir('dmsrc')

outfilename = 'rust_g.dm'
directory = sorted(glob.glob('*.dm'))

with open(outfilename, 'wb') as outfile:
    for file in directory:
        if file == outfilename:
            # don't want to copy the output into the output
            continue
        with open(file, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)


