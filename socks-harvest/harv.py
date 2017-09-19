#!/usr/bin/env/ python

#
# demo script that harvests socks proxy addresses
#

import re
import requests


url = 'reducted'
res = requests.get(url)

ports = []
ips = []

regex1 = re.compile('\=([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:')
regex = re.compile('\^([0-9]{1,5})\)\ ')
for line in res:
     ips += regex1.findall(line)
     ports += regex.findall(line)

for i in range(len(ips)):
    print ips[i]+':'+ports[i]
    
