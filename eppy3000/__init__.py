# -*- coding: utf-8 -*-

"""Top-level package for eppy3000."""

__author__ = """Santosh Philip"""
__email__ = "santosh@noemail.com"
__version__ = "0.1.4"

import os

from .modelmaker import EPJ


def is_path(arg):
    try:
        os.fspath(arg)
        return True
    except TypeError:
        return False


def get_filehandler(arg):
    if is_path(arg):
        return open(arg, "rt")
    elif hasattr(arg, "read"):
        return arg
    else:
        raise TypeError(
            f"expected str, bytes, os.PathLike object or file object, not {type(arg)}"
        )


def epj(epj, epschema=None):
    """The wrapper function for the EPJ object.

    Parameters
    ----------
    epj : str, bytes, os.PathLike object or file object
    epschema : str, bytes, os.PathLike object or file object

    """
    epj_fh = get_filehandler(epj)
    epschema_fh = get_filehandler(epschema) if epschema else None
    epj = EPJ(epj_fh, epschema_fh)
    if is_path(epj):
        epj_fh.close()
        epj.epj_filename = epj
    if epschema and is_path(epschema):
        epschema_fh.close()
        epj.epschema_filename = epschema
    return epj
