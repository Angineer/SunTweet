class datum:
	def __init__(self, dataSource):
		"""Initializes datapoint

		Arguments
		path: The location of the data stream from which to read.
			Should be a text file with the following format:
				date time datavalue
			on each line
		"""
		self.dataSource=dataSource
		self.date="01/01/2000"
		self.time="00:00"
		self.value=0

	def Update(self):
		"""Update the datapoint to have the most recent value from the data stream"""
		#Read in raw data
		with open(self.dataSource, 'r') as dataFile:
			dataFile.seek(-22, 2)
			line=dataFile.read(22)
		
		#Parse data
		lineList=line.split()
		date=lineList[0]
		time=lineList[1]
		value=lineList[2]

		#Set to new value
		self.date=date
		self.time=time
		self.value=value

	def GetDateTime(self):
		return self.date+" "+self.time

	def GetValue(self):
		return self.value