
# ===========================
# 1.infer using two files(0 and 1)
# 2.delete 2 files
# 3.return result
# ============================

import glob
import re
import os

from . import similarity

def face_similarity():
    result = similarity.facenet()
    return result

def file_delete():
    pathes = glob.glob('/root/enjoy_cording_with_python/Twins-detection/ai/images/*.jpg')
    for path in pathes:
        result = os.remove(path)

def infer():
    result = face_similarity()
    file_delete()

    return str(result)