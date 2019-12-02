import os
import sys

try:
    import codecs
except ImportError:
    codecs = None

try:
    import thread
    import threading
except ImportError:
    thread = None

try:
    unicode
    _unicode = True
except NameError:
    _unicode = False


def currentframe():
    """Return the frame object for the caller's stack frame."""
    try:
        raise Exception
    except:
        return sys.exc_info()[2].tb_frame.f_back


if hasattr(sys, '_getframe'): currentframe = lambda: sys._getframe(3)

_srcfile = os.path.normcase(currentframe.__code__.co_filename)


def findCaller():
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    # On some versions of IronPython, currentframe() returns None if
    # IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    rv = "(unknown file)", 0, "(unknown function)"
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        rv = (co.co_filename, f.f_lineno)
        break
    return rv
