#! /usr/bin/env python

import sys
import os
import urllib2
import time
import json
import string
import datetime
import random
import getopt



datadir = '/home/juyun/datafile'
newrelickey = '19e4cb7a2ec9c43a7a90cec3360fb7b5868d08d6'
pluginname = 'ClearClouds'
juyuninidir = '/usr/local/etc'
juyunini_newrelic = juyuninidir + '/newrelic.ini'




def post_data(url, data):

	global newrelickey

	try:
		request = urllib2.Request(url, data, {'X-License-Key': newrelickey, 'Content-Type': 'application/json', 'Accept': 'application/json'})
		response = urllib2.urlopen(request)
		if response.getcode() != 200:
			print 'post status code:', response.getcode()
		else:
			print response.read()
	except Exception, e:
		print 'post exception:', str(e)



def post_newrelic(data):
	url = 'https://platform-api.newrelic.com/platform/v1/metrics'
	post_data(url, data)






def format_newrelicdata_from_dictdata(dictdata):

	global pluginname

	header = """
	{
		"agent": {
			"host" : "test.clearclouds.com",
			"pid" : 1234,
			"version" : "1.0.0"
		},
		"components": [		
			{
				"name": "%s",
				"guid": "com.clearclouds.Clearclouds",
				"duration" : 60,
				"metrics" : {
					"""



	footer = """
				}
			}
		]
	}
	"""


	strdata = ""
	seperator = ""
	# seperator = "					"
	i = 0 
	for firstkey,firstvalue in dictdata.items() :
		if i == 0 :
			strdata = seperator + '"' + firstkey + '" : ' + str(firstvalue)
		else :
			strdata = strdata + ',' + seperator + '"' + firstkey + '" : ' + str(firstvalue)

		i = i + 1 


	global pluginname 


	strdata =  (header + strdata + footer)   % ('Clearclouds')




	# get_commandline() 
	# print(strdata)
	# sys.exit(1)


	return strdata






def parse_jsons():

	rands = random.randint(1,100)


	data = {}
	dictdata = {
		"Component/Test/A[Bytes]" : rands
	}




	data = format_newrelicdata_from_dictdata(dictdata)
	post_newrelic(data)





def ExcuteFetcher():

	while True:

		parse_jsons()

		time.sleep(5)


	return 0





def main():


	opts,args = getopt.getopt(sys.argv[1:], "rthd:k:n:", ["help"])

	print(opts)


	if opts == [] :

		print("no argment")
		sys.exit(1);  



	# ExcuteFetcher()





if __name__ == '__main__':

	main()


# main()

# exit(main())