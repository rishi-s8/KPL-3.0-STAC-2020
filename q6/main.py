# all imports below
import math
"""
Any extra lines of code (if required)
as helper for this function.
"""
def findstrike(v, alt, az):
'''
Parameters
----------
velocity : A `float`
alt: A `float`
az: A `float`

Returns
-------
A `tuple` of two floats
    '''
    g=9.8
    h=8848
    range=math.sqrt((2*v**2)*(h+(v**2/2*g))/g)

    r1=6371000+h
    p1=az
    q1=90-alt

    x1=r1*math.sin(q1)*math.cos(p1)
    y1=r1*math.sin(q1)*math.sin(p1)
    z1=r1*math.cos(q1)

    p=90-27.9881
    q=86.9250

    r2=range
    r=math.sqrt(r1**2+r2**2)

    x=math.sqrt(r**2/(1+(math.tan(p))**2)*(1+1/(math.tan(q)**2)))
    y=x*math.tan(p)
    z=x*math.sqrt((1+(math.tan(p))**2)/(math.tan(q)**2))

    x2=x-x1
    y2=y-y1
    z2=z-z1

    long=math.atan(y2/x2)
    lat=90-math.atan(math.sqrt((x2**2+y2**2)/z2**2))

    return (lat, long)





        
