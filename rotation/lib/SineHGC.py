# coding: utf-8
"""
Class to implement a new coordinate system and its conversions
"""
import astropy.units as u
import sunpy.coordinates as spc
import astropy.coordinates as coord
from astropy.coordinates import frame_transform_graph

class SineHGC(spc.HeliographicCarrington):
    """
    A Frame to represent the Sine(Carrington Latitude) frame.

    The latitude in this frame has units degrees 
    even though it is unitless for simplicity.
    As Astropy does not support something that is
    latitude-like and not in angular units.
    """

@frame_transform_graph.transform(coord.FunctionTransform,
        spc.HeliographicCarrington, SineHGC)
def hgc_to_sinehgc(hgc_coord, sinehgc_frame):
    lat = hgc_coord.lat
    lon = hgc_coord.lon
    lat_out = u.Quantity(np.sin(lat.value), u.rad)
    return sinehgc_frame.realize_frame(
            coord.UnitSphericalRepresentation(lat=lat_out, lon=lon))


@frame_transform_graph.transform(coord.FunctionTransform, SineHGC,
            spc.HeliographicCarrington)
def sinehgc_to_hgc(sinehgc_coord, hgc_frame):
    lat = sinehgc_coord.lat
    lon = sinehgc_coord.lon
    lat_out = u.Quantity(np.arcsin(lat.value), u.rad)
    return hgc_frame.realize_frame(
            coord.UnitSphericalRepresentation(lat=lat_out, lon=lon))



