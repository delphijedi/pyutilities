import os
import re
import urllib2

def check_in():
	
	fqn = os.uname()[1]
	ext_ip = urllib2.urlopen('http://whatismyip.org').read()
	ip = re.findall(r'[0-9]+(?:.[0-9]+){3}',ext_ip)
#	print ("Asset: %s " % fqn, "Checking in from ip: %s " % ext_ip)
	print ("External IP is %s " % ip)

