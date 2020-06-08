# all imports below

from astroplan import Observer, FixedTarget
from astropy.time import Time
from datetime import datetime
import numpy as np
import astropy
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris,SkyCoord, EarthLocation, AltAz
"""
Any extra lines of code (if required)
as helper for this function.
"""

startobs = datetime(2020, 6, 8, 16, 48, 31) #replace it by the time when Saturn will be just visible
endobs = datetime(2020, 6, 9, 3, 2, 17) #replace it by the time when Saturn is no longer visible from SAC terrace

def findSaturn(obstime):
    '''
    Parameters
    ----------
    obstime : A `~datetime.datetime` instance.

    Returns
    -------
    A `tuple` of two floats.
    '''


    co=astropy.coordinates.get_body(body='saturn',time=Time(obstime),location=None)
    ti=Time(obstime)
    mandi=EarthLocation(lat=31.775461*u.deg, lon=76.98600769042969*u.deg,height=1000*u.m)
    alt=co.transform_to(AltAz(obstime=ti,location=mandi))
    source = Observer(location=mandi)
    azm=alt.secz

    saturn_set_time = source.target_set_time(Time(obstime), co, which="nearest")
    saturn_rise_time = source.target_rise_time(Time(obstime), co, which="nearest")

    return (source.astropy_time_to_datetime(saturn_rise_time), source.astropy_time_to_datetime(saturn_set_time))
