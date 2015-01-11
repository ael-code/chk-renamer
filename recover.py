import sys
import os
import mimetypes
from pprint import pprint
import subprocess

usage = sys.argv[0] + " CORRUPTED_PATH(s) RECOVER_FOLDER"

if len(sys.argv) < 3:
    print (usage)
    sys.exit(1)

def getMime(file):
    res = subprocess.check_output(["/usr/bin/file", "-b", "--mime-type", file],universal_newlines=True)
    return res[:len(res)-1]

def getExt(mime):
    return mimetypes.guess_extension(mime)
corrPaths = []
recoverPath = sys.argv[len(sys.argv)-1]

stats = {}

for i in range(1,len(sys.argv)-1):
    if not os.path.isdir(sys.argv[i]):
        raise Exception("CORRUPTED_PATH not a folder")
    corrPaths.append(sys.argv[i])

for folder in corrPaths:
    print "folder: "+folder
    for f in os.listdir(folder):
        file = os.path.join(folder,f)       
        mime = getMime(file)
        ext = getExt(mime)
        if mime not in stats:
            stats[mime] = 1
        else:
            stats[mime] = stats[mime]+1     
        print "    file: {} ext:{} ({})".format(file,ext,mime)

pprint( stats )


