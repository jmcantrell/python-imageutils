from decimal import Decimal
from PIL import Image


def gcf(x, y):  # {{{1
    """Gets the greatest common denominator of the arguments.
    >>> gcf(640, 480)
    160
    """
    while y:
        x, y = y, x % y
    return x


def aspect_ratio(size):  # {{{1
    """Gets the aspect ratio of the given size tuple.
    >>> aspect_ratio((640, 480))
    (4, 3)
    >>> aspect_ratio((4, 3))
    (4, 3)
    """
    d = gcf(*size)
    return tuple(v/d for v in size)


def aspect_ratio_approximate(size):  # {{{1
    """Gets a decimal approximation of an aspect ratio.
    >>> aspect_ratio_approximate((640, 480))
    Decimal('1.33')
    >>> aspect_ratio_approximate((4, 3))
    Decimal('1.33')
    """
    return Decimal('%.2f' % (float(size[0])/size[1]))


def same_aspect_ratio(size1, size2):  # {{{1
    """Determines if two sizes have the same aspect ratio.
    >>> same_aspect_ratio((640, 480), (4, 3))
    True
    >>> same_aspect_ratio((1280, 1024), (4, 3))
    False
    """
    return aspect_ratio_approximate(size1) == aspect_ratio_approximate(size2)


def safe_resize(image, sizer):  # {{{1
    """Resizes an image only if it's needed."""
    if None in sizer:
        sizer = scale_size(image.size, sizer)
    if image.size == sizer:
        return image
    return image.resize(sizer, Image.ANTIALIAS)


def scale_size(size, sizer):  # {{{1
    """Scales a size tuple based on a sizer tuple.
    A sizer is just a size tuple that specifies only width or height.
    >>> scale_size((640, 480), (800, None))
    (800, 600)
    >>> scale_size((640, 480), (None, 3))
    (4, 3)
    """
    if not any(sizer):
        return size
    size_new = list(sizer)
    i = size_new.index(None)
    j = i * -1 + 1
    size_new[i] = (size_new[j] * size[i]) / size[j]
    return tuple(size_new)


def scale(size_bg, size_fg):  # {{{1
    """Scales one size to fit inside another.
    >>> scale((400, 400), (100, 100))
    (400, 400)
    >>> scale((100, 100), (400, 400))
    (100, 100)
    >>> scale((600, 400), (500, 500))
    (400, 400)
    """
    size_fg = scale_size(size_fg, (size_bg[0], None))
    size_fg = scale_size(size_fg, (None, size_bg[1]))
    return size_fg


def scale_down(size_bg, size_fg):  # {{{1
    """Scales one size to fit inside another.
    Will only scale down, never up.
    >>> scale_down((100, 100), (400, 400))
    (100, 100)
    >>> scale_down((400, 400), (100, 100))
    (100, 100)
    """
    if size_fg[0] > size_bg[0] or size_fg[1] > size_bg[1]:
        return scale(size_bg, size_fg)
    return size_fg


def scale_up(size_bg, size_fg):  # {{{1
    """Scales one size to fit inside another.
    Will only scale up, never down.
    >>> scale_up((100, 100), (400, 400))
    (400, 400)
    >>> scale_up((400, 400), (100, 100))
    (400, 400)
    """
    if size_fg[0] < size_bg[0] or size_fg[1] < size_bg[1]:
        return scale(size_bg, size_fg)
    return size_fg


def center(size_bg, size_fg):  # {{{1
    """Get the centering coordinates for fg against bg.
    >>> center((800, 600), (640, 480))
    (80, 60)
    >>> center((640, 480), (800, 600))
    (-80, -60)
    """
    cw = center_edge(size_bg[0], size_fg[0])
    ch = center_edge(size_bg[1], size_fg[1])
    return cw, ch


def center_edge(bg_edge, fg_edge):  # {{{1
    """Get the offset needed to center fg relative to bg.
    >>> center_edge(100, 50)
    25
    """
    return (bg_edge - fg_edge) / 2
