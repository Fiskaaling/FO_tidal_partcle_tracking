import numpy as np

# Definitions used in geo.js

#Convert geographical latitude and longitude to matrix index (x,y)
def geo2grid(lon,lat):

	rad = 180 / np.pi  # Define one radian
	crop = 0  # How many cells have been cropped from the original matrix
	ewpivot = (-7) / rad  # Pivot point of the matrix
	onedgr = 1852 * 60  # One angular degree
	orgHeight = 1501  # Height of original matrix

	rlon=lon/rad-ewpivot
	rlat=lat/rad
	alat  = np.arcsin(np.sin(rlon)*np.cos(rlat))
	ydisp = np.arcsin(np.sin(rlat)/np.cos(alat))
	southb =  61.2/rad
	gridn  = 100/onedgr
	miry =  orgHeight - (1+(ydisp-southb)*rad/gridn) -crop
	y = (744-miry)+744
	dist=np.log(np.tan((2*alat+np.pi)/4))*rad/gridn
	x = (0.5*1075+dist)
	returnVal = [x,y]
	return returnVal


# def grid2geo(x,y, width):
# 	gridn  = 100/onedgr/rad
# 	southb =  61.2/rad
# 	xpivn = 0.5*width
# 	y = 1501-y-crop
# 	latn=alat(x-xpivn,gridn)
# 	ydist=(y-1)*gridn
# 	ydist = ydist + southb
# 	rlat =np.arcsin(np.sin(ydist)* np.cos(latn))
# 	rlon =ewpivot+np.arcsin(np.sin(latn)/np.cos(rlat))
# 	lat=rlat*rad
# 	lon=rlon*rad
# 	return [lat,lon]


# def drawSquare(xstart, ystart, diam, context,color):
#
# 	diam = np.ceil(diam)
# 	xstart = np.round(xstart -(diam/2))
# 	ystart = np.round(ystart - (diam/2))
# 	context.beginPath();
# 	context.rect(xstart, ystart, diam+1, diam+1);
# 	context.fillStyle = color;
#     context.fill();