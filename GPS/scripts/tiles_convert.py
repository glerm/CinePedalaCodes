#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import math, sys

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return (xtile, ytile)


def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)

M=deg2num(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))

X=str(M[0])
Y=str(M[1])
ZOOM=sys.argv[3]

print "++++++++++++++++\n"
print "zoom= "+ ZOOM +"\n"
print "x= "+ X +"\n"
print "y= "+ Y +"\n\n"
print "\n\n URL= http://tile.openstreetmap.org/"+ZOOM+"/"+X+"/"+Y+".png\n\n" 


