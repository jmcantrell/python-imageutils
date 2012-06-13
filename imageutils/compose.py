from . import size


def paste_scale(bg, fg):  # {{{1
    """Scales maximally and centers the fg onto bg."""
    ar_fg = size.aspect_ratio(fg.size)
    ar_bg = size.aspect_ratio(bg.size)
    if ar_fg == ar_bg:
        sz = bg.size
        box = None
    elif ar_fg < ar_bg:
        sz = size.scale_size(fg.size, (None, bg.size[1]))
        c = size.center_edge(bg.size[0], sz[0])
        box = (c, 0, c + sz[0], bg.size[1])
    else:
        sz = size.scale_size(fg.size, (bg.size[0], None))
        c = size.center_edge(bg.size[1], sz[1])
        box = (0, c, bg.size[0], c + sz[1])
    fg = size.safe_resize(fg, sz)
    bg.paste(fg, box)
    return bg


def paste_zoom(bg, fg):  # {{{1
    """Scales the centered fg onto bg such that fg completely covers bg."""
    fg_ar = size.aspect_ratio(fg.size)
    bg_ar = size.aspect_ratio(bg.size)
    if fg_ar == bg_ar:
        sz = bg.size
        box = None
    elif fg_ar < bg_ar:
        sz = size.scale_size(fg.size, (bg.size[0], None))
        c = size.center_edge(bg.size[1], sz[1])
        box = (0, c, bg.size[0], c + sz[1])
    else:
        sz = size.scale_size(fg.size, (None, bg.size[1]))
        c = size.center_edge(bg.size[0], sz[0])
        box = (c, 0, c + size[0], bg.size[1])
    fg = size.safe_resize(fg, sz)
    bg.paste(fg, box)
    return bg


def paste_stretch(bg, fg):  # {{{1
    """Pastes fg with the exact dimensions of bg onto bg."""
    bg.paste(size.safe_resize(fg, bg.size))
    return bg


def paste_center(bg, fg):  # {{{1
    """Pastes the centered fg onto bg with no resizing."""
    cw = size.center_edge(bg.size[0], fg.size[0])
    ch = size.center_edge(bg.size[1], fg.size[1])
    bg.paste(fg, (cw, ch))
    return bg


def paste_tile(bg, fg):  # {{{1
    """Pastes multiple copies of fg onto bg in a tiled pattern."""
    nw = bg.size[0] / fg.size[0] + 1
    nh = bg.size[1] / fg.size[1] + 1
    for t in range(nh):
        for l in range(nw):
            bg.paste(fg, (l * fg.size[0], t * fg.size[1]))
    return bg
