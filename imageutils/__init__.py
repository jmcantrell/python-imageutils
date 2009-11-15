import os

__all__ = ['color', 'size', 'compose']

IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

def valid_image(fn): #{{{1
    """Test whether or not a filename is a common image format.
    >>> valid_image('foo.jpg')
    True
    >>> valid_image('bar.txt')
    False
    """
    extension = os.path.splitext(fn)[1].lstrip('.').lower()
    if extension in IMAGE_EXTENSIONS: return True
    return False

def find_images(directory): #{{{1
    """Finds all images in a directory (recursive)."""
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            ld = os.path.join(root, d)
            if not os.path.islink(ld): continue
            for img in find_images(ld):
                yield img
        for f in files:
            img = os.path.join(root, f)
            if not valid_image(img): continue
            yield img
