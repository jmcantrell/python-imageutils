import os
from PIL import Image

__all__ = ['color', 'size', 'compose']

def find_images(directory): #{{{1
    """Finds all images in a directory (recursive)."""
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            ld = os.path.join(root, d)
            if not os.path.islink(ld): continue
            for img in find_images(ld):
                yield img
        for f in files:
            try:
                yield Image.open(os.path.join(root, f))
            except:
                continue
