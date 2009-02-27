from decimal import Decimal
from PIL import Image

def gcf(x, y): #{{{1
    """Gets the greatest common denominator of the arguments.
    >>> gcf(640, 480)
    160
    """
    while y:
        x, y = y, x % y
    return x

def aspect_ratio(size): #{{{1
    """Gets the aspect ratio of the given size tuple.
    >>> aspect_ratio((640, 480))
    (4, 3)
    >>> aspect_ratio((4, 3))
    (4, 3)
    """
    d = gcf(*size)
    return tuple(v/d for v in size)

def aspect_ratio_approximate(size): #{{{1
    """Gets a decimal approximation of an aspect ratio.
    >>> aspect_ratio_approximate((640, 480))
    Decimal("1.33")
    >>> aspect_ratio_approximate((4, 3))
    Decimal("1.33")
    """
    return Decimal('%.2f' % (float(size[0])/size[1]))

def same_aspect_ratio(size1, size2): #{{{1
    """Determines if two sizes have the same aspect ratio.
    >>> same_aspect_ratio((640, 480), (4, 3))
    True
    >>> same_aspect_ratio((1280, 1024), (4, 3))
    False
    """
    return aspect_ratio_approximate(size1) == aspect_ratio_approximate(size2)

def safe_resize(image, sizer): #{{{1
    """Resizes an image only if it's needed."""
    if None in sizer: sizer = scale_size(image.size, sizer)
    if image.size == sizer: return image
    return image.resize(sizer, Image.ANTIALIAS)

def scale_size(size, sizer): #{{{1
    """Scales a size tuple based on a sizer tuple.
    A "sizer" is just a size tuple that specifies only width or height.
    >>> scale_size((640, 480), (800, None))
    (800, 600)
    >>> scale_size((640, 480), (None, 3))
    (4, 3)
    """
    if not any(sizer): return size
    size_new = list(sizer)
    i = size_new.index(None)
    j = i * -1 + 1
    size_new[i] = (size_new[j] * size[i]) / size[j]
    return tuple(size_new)

def center_edge(bg_edge, fg_edge): #{{{1
    """Given the two lengths, this will give the offset needed to center the
    second relative to the first.
    >>> center_edge(100, 50)
    25
    """
    return (bg_edge - fg_edge) / 2
