# SunTweet
# This script will tweet about the sun

import time
import twitter
from Sun import *
from authorize import authorize

#Start up a twitter API
api=authorize()

#Create a new data point to monitor
solarDataPoint=datum("/home/andy/Dropbox/Projects/Python/SunTweet/test.txt")

#Update the data point every 15 minutes
lastTime=time.time()
lastSolarTime=solarDataPoint.GetDateTime()
while True:
	currTime=time.time() #Check current time
	if (currTime>=lastTime+15*60):
		solarDataPoint.Update()
		solarTime=solarDataPoint.GetDateTime()
		solarValue=solarDataPoint.GetValue()

		if (solarTime!=lastSolarTime): #Make sure log is being updated
			if (solarValue>10): #Based on the value of the data point, tweet about it
				api.PostUpdate("The sun is currently shining at "+solarValue+" watts")

			lastSolarTime=solarTime
		else:
			print "Log dupe"

		lastTime=currTime
	time.sleep(60) #Wait 1 minute before trying again

#api.ClearCredentials()