# SunTweet
# This script will tweet about the sun

import time
import twitter
import Sun
from authorize import authorize

#Start up a twitter API
try:
	api=authorize()
except:

#Create a new data point to monitor
solarDataPoint=datum("/home/andy/solarOutput.txt")

#Update the data point every 15 minutes
lastTime=time.clock()
while True:
	currTime=time.clock() #Check current time
	if (currTime>lastTime+15*60):
		solarDataPoint.Update()
		solarValue=solarDataPoint.GetValue()

		#Based on the value of the data point, tweet about it
		if (solarValue>0):
			api.PostUpdate("The sun is currently shining at "+solarValue+" watts")

		currTime=time
	time.sleep(60) #Wait 1 minute before trying again

api.ClearCredentials()