# import subprocess
# subprocess.Popen('explorer "C:\Thameem\Testing\mamooth"')

import os
import zipfile

zf = zipfile.ZipFile("myzipfile.zip", "w",zipfile.ZIP_DEFLATED)
for dirname, subdirs, files in os.walk(r"C:\Thameem\POC_CODE\demo"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()