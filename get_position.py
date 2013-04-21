import urllib
import urllib2
import re
f = open('data/ISS030-E-114986/ISS030-E-114986.txt')
lines = f.readlines()
f.close()
print lines[1]
data=re.split('\t|\r| |:', lines[1])
mission="030s"
year= data[5]
month= data[6]
day= data[7]
hour= data[8]
minute= data[9]
seconds= data[10]
url = 'http://eol.jsc.nasa.gov/time2pos/default.htm'
form_data = {"mission":mission,"year":year,"month":month,"day":day,"hour":hour,"minute":minute,"second":seconds}
params = urllib.urlencode(form_data)
url2="http://eol.jsc.nasa.gov/scripts/time2pos/runtime2pos.pl"
response = urllib2.urlopen(url2, params)
data = response.readlines()
print data[2]
print data[3]
