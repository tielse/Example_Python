import pygeoip
# http://code.google.com/p/pygeoip/
gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')
def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' + tgt + ' Geo-located. '
	print '[ +] ' +str(city) +', ' +str(region) +', ' +str(country)
	print '[ +] Latitude: ' +str(lat) + ', Longitude: ' + str(long)
tgt = '192.168.1.107'
printRecord(tgt)