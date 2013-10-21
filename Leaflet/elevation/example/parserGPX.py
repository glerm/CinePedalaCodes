#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import xmltodict, json
from xml.dom.minidom import parse



GPX_dom = parse("feira.gpx")
GPX_str=GPX_dom.toxml()
GPX_dict = xmltodict.parse(GPX_str)

trackpts=len(GPX_dict['gpx']['trk']['trkseg']['trkpt'])

def printTRK():
	for i in xrange(trackpts):
		print "+++++++++ Ponto [ "+ str(i) + " ]+++++++++++\n"	
		print "latitude= [ "+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['@lat'])+ " ]\n"
		print "longitude= [ "+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['@lon'])+ " ]\n"
		print "elevacao= [ "+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['ele'])+ " ]\n"
		print "tempo= [ "+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['time'])+ " ]\n"

def PDTRK():
	for i in xrange(trackpts):
		print "latitude "+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['@lat'])
		print "longitude "+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['@lon'])

def leafletGPX():
	for i in xrange(trackpts):
		print "["+str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['@lat'])+","+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['@lon'])+ ","+ str(GPX_dict['gpx']['trk']['trkseg']['trkpt'][i]['ele'])+"], "





#PDTRK()

#printTRK() #debug

leafletGPX()


################### marcações #############
#marcas=GPX_dict['gpx']['wpt']
#marcaspts=len(marcas)

#for j in xrange(marcaspts):
#	print str(marcas[j])+"\n\n"	


#for j in xrange(marcaspts):
#	print str(marcas[j]['name'])+"\n\n"	#resolver acentuação na impressão
