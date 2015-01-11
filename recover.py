import sys
import os
import mimetypes
from pprint import pprint
import magic
import shutil

usage = sys.argv[0] + " CORRUPTED_PATH(s) RECOVER_FOLDER"

if len(sys.argv) < 3:
    print (usage)
    sys.exit(1)

def getMime(file):
    return magic.from_file(file, mime=True)

def getExt(mime):
    return mimetypes.guess_extension(mime)

corrPaths = []
recoverPath = sys.argv[-1]

stats = {}

try:
    os.makedirs(recoverPath)
except OSError, e:
    pass

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
        if not ext:
            ext = "bho"
        fileDst = os.path.join(recoverPath,f[:-4]+ext)
        print "    file: {} ({}) to {}".format(file,mime,fileDst)
        shutil.copyfile(file,fileDst)

pprint( stats )
