import os
from PIL import Image
from PIL.ExifTags import TAGS

__all__ = ['color', 'size', 'compose']


def find_images(directory):
    """Finds all images in a directory (recursive)."""
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            ld = os.path.join(root, d)
            if not os.path.islink(ld):
                continue
            for img in find_images(ld):
                yield img
        for f in files:
            try:
                yield Image.open(os.path.join(root, f))
            except:
                continue


def get_exif(filename):
    ret = {}
    i = Image.open(filename)
    info = i._getexif()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
    return ret
