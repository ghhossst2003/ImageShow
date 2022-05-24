# coding = 'utf-8'

import os
import uuid
from filetype import filetype
from image import save_image


def getFileExtraName(fileName):
    return os.path.splitext(fileName)[-1]


def getFileName(fileName):
    extraName = getFileExtraName(fileName)
    return '%s%s' % (uuid.uuid1(), extraName)


def savePath(path, fileName):
    return os.path.join(path, fileName)


def fileType(path):
    kind = filetype.guess(path)
    if kind is None:
        raise "file file is error"
    return kind.extension


def save_file(path, f):
    new_filename = getFileName(f.filename)
    new_path = savePath(path, new_filename)
    f.save(new_path)
    return save_image(f.filename, new_filename, new_path, fileType(new_path))
