#!/usr/bin/env python

import random
import sys, getopt

def randip():
	m = []
	for i in xrange(4):
		m.append(random.randint(0,255))
	return ".".join(map(lambda x:"%d"%x,m))

def iptoint(ip): # converts string ip to integer ip, i.e str '192.168.1.1' to int 192168001001
	return int(''.join([str("%03d"%i) for i in map(int,ip.split('.'))]))

def inttoip(integ): # converts integer ip to string ip, i.e int 192168001001 to str '192.168.1.1'
	integ = str(integ)
	lis = []
	for i in range(0,len(integ), 3):
		p = int(integ[i:i+3])
		if p<10:
			p = "%01d"%p
		elif p<100:
			p = "%02d"%p
		lis.append(str(p))
	return lis[0]+'.'+lis[1]+'.'+lis[2]+'.'+lis[3] 

def rangeipgen(start, stop):
	temp = start
	rangeip = []
	rangeip.append(".".join(map(str, temp)))
	while temp != stop:
		start[3] += 1
		for i in (3, 2, 1):
			if temp[i] == 256:
				temp[i] = 0
				temp[i-1] += 1
		rangeip.append(".".join(map(str, temp)))    
	             
	return rangeip

def rangewrite(start, stop, f):
	lis = rangeipgen(start, stop)
	for i in lis:
		f.write("%s\n" %i)
	return

def helpmenu():
	print 'Random ip generator\nUsage: ip-gen.py [options]\n'
	print '  -h,  --help			Print this help'
	print '  -o,  --output-file=filename	Choose an output file'
	print '  -r,  --range=ip1-ip2		Generate ips between this range(ip1<=ips<=ip2)'
	print '  -n,  --number=X		Choose the number of desired ips to generate\n'

def usage():
	print 'ip-gen.py\nUsage: ip-gen.py [options]\n\nTry \'ip-gen.py -h\' for more options.'
	return

def main(argv):
	number = 0
	outputfile = 0
	start = 0
	try:
		opts, args = getopt.getopt(argv,"ho:n:r:",["help","output-file=","range=","number="])
	except getopt.GetoptError:
		usage()
		exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			helpmenu()
			exit()
		elif opt in ("-o", "--output-file"):
			try:
				open(arg, 'a')
			except:
				print("You don't have permission to access this file.\nTry another filename.")
				exit()
			outputfile = arg
		elif opt in ("-n", "--number"):
			number = int(arg)
		elif opt in ("-r", "--range"):
			try:
				srt = iptoint(arg.split("-")[0])
				stp = iptoint(arg.split("-")[1])
				if srt > stp:
					usage()
					exit()
				start = list(map(int, arg.split("-")[0].split(".")))
				stop  = list(map(int, arg.split("-")[1].split(".")))
			except:
				usage()
				exit()
		else:
			usage()

	if not number:
		if (not outputfile) and (not start):
			print randip()
		elif outputfile and (not start):
			with open(outputfile, 'a') as f:
				f.write(randip()+'\n')
		elif (not outputfile) and start:
			lis = rangeipgen(start, stop)
			for i in lis:
				print("%s" %i)
		elif outputfile and start:
			with open(outputfile, 'a') as f:
				rangewrite(start, stop, f)
	else:
		if (not outputfile) and (not start):
			for i in xrange(number):
				print randip()
		elif outputfile and start:
			with open(outputfile, 'a') as f:
				for i in xrange(number):
					f.write(randip()+'\n')
				rangewrite(start, stop, f)
		elif (not outputfile) and start:
	                lis = rangeipgen(start, stop)
        	        for i in lis:
				print("%s" %i)
			for i in xrange(number):
				print randip()
		elif outputfile and (not start):
			with open(outputfile, 'a') as f:
				for i in xrange(number):
					f.write(randip()+'\n')

if __name__ == "__main__":
	main(sys.argv[1:])
