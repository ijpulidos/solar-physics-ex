# coding: utf-8
"""
Python module to make corrections and conversions from wrong formatted 
HMI fits files
"""

import astropy.wcs.utils
from astropy.wcs import WCSSUB_CELESTIAL

from lib.SineHGC import SineHGC

def sinehpc_wcs_frame_mapping(wcs):
    """
    This function registers the coordinates frames to their FITS-WCS coordinate
    type values in the `astropy.wcs.utils.wcs_to_celestial_frame` registry.
    """
    # Get dateobs fromt the wcs
    dateobs = wcs.wcs.dateobs if wcs.wcs.dateobs else None

    # First we try the Celestial sub, which rectifies the order. It will return
    # any thing matching ??LN*, ??LT*
    wcss = wcs.sub([WCSSUB_CELESTIAL])

    # If the SUB works, use it.
    if wcss.naxis == 2:
        wcs = wcss

    xcoord = wcs.wcs.ctype[0][0:4]
    ycoord = wcs.wcs.ctype[1][0:4]

    if xcoord == 'CSLN' and ycoord == 'CSLT':
        return SineHGC(dateobs=dateobs)


