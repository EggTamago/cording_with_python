
# ===========================
# 1.infer using two files(0 and 1)
# 2.delete 2 files
# 3.return result
# ============================

import glob
import re
import os

from . import similality

def face_similarity():
    


def file_delete():

    pathes = glob.glob('images/*.jpg')
    for path in pathes:
        result = os.remove(path)

def infer():
    return 'ok'

if __name__ == '__main__':
    file_delete()