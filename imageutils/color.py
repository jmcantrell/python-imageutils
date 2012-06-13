from PIL import ImageColor

COLOR_NAME_HEX = ImageColor.colormap
COLOR_HEX_NAME = dict((v, k) for k, v in COLOR_NAME_HEX.iteritems())


def hex_to_name(value):  # {{{1
    """Gets a color name (if it exists) for a hex color value.
    >>> hex_to_name('#000000')
    'black'
    """
    if not value.startswith('#'):
        value = '#' + value
    return COLOR_HEX_NAME.get(value)


def name_to_hex(value):  # {{{1
    """Gets a hex value for a color name.
    >>> name_to_hex('black')
    '#000000'
    """
    return COLOR_NAME_HEX.get(value)


def hex_max(value):  # {{{1
    """Gets the maximum color channel value for a hex color value.
    >>> hex_max('#ddeeff')
    255
    >>> hex_max('#00001111aaaa')
    65535
    """
    value = value.lstrip('#')
    return int('f' * (len(value)/3), 16)


def rgb16_to_rgb8(value):  # {{{1
    """Scales a 16-bit RGB tuple to an 8-bit value.
    >>> rgb16_to_rgb8((65535, 65535, 65535))
    (255, 255, 255)
    """
    return tuple(int(v/257.0) for v in value)


def rgb8_to_rgb16(value):  # {{{1
    """Scales an 8-bit RGB tuple up to a 16-bit value.
    >>> rgb8_to_rgb16((255, 255, 255))
    (65535, 65535, 65535)
    """
    return tuple(v*257 for v in value)


def rgb_to_rgb_percent(value, bpc):  # {{{1
    """Converts an RGB tuple to a percentage.
    >>> rgb_to_rgb_percent((255, 255, 255), 255)
    (100, 100, 100)
    >>> rgb_to_rgb_percent((65535, 65535, 65535), 65535)
    (100, 100, 100)
    """
    return tuple(int(float(v)/bpc)*100 for v in value)


def rgb_percent_to_rgb(value, bpc):  # {{{1
    """Converts an RGB percentage to a normal value.
    >>> rgb_percent_to_rgb((100, 100, 100), 255)
    (255, 255, 255)
    >>> rgb_percent_to_rgb((100, 100, 100), 65535)
    (65535, 65535, 65535)
    """
    return tuple(int(bpc*(v/100.0)) for v in value)


def hex_to_rgb_percent(value):  # {{{1
    """Converts a hex color value to an RGB percentage.
    >>> hex_to_rgb_percent('#ffffff')
    (100, 100, 100)
    >>> hex_to_rgb_percent('#ffffffffffff')
    (100, 100, 100)
    """
    value = value.lstrip('#')
    rgb = hex_to_rgb(value)
    bpc = hex_max(value)
    return rgb_to_rgb_percent(rgb, bpc)


def hex_to_rgb(value):  # {{{1
    """Converts a hex color value to an RGB tuple.
    >>> hex_to_rgb('#ffffff')
    (255, 255, 255)
    >>> hex_to_rgb('#ffffffffffff')
    (65535, 65535, 65535)
    """
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))


def short_hex_to_hex(value):  # {{{1
    """Normalizes a shorthand hex value commonly used in CSS.
    >>> short_hex_to_hex('#fff')
    '#ffffff'
    """
    value = value.lstrip('#')
    if len(value) == 6:
        return '#' + value
    return '#' + ''.join(v*2 for v in value)


def rgb_to_hex(rgb):  # {{{1
    """Converts an RGB tuple to a hex color value.
    >>> rgb_to_hex((255, 255, 255))
    '#ffffff'
    """
    return '#%02x%02x%02x' % rgb
