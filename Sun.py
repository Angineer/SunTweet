class datum:
	def __init__(self, dataSource):
		"""Initializes datapoint

		Arguments
		path: The location of the data stream from which to read.
			Should be a csv document with the following format:
				timestamp, datavalue
			on each line
		"""
		self.dataSource=dataSource
		self.value=0

	def Update(self):
		"""Update the datapoint to have the most recent value from the data stream"""
		#Read in raw data
		new=0

		#Set to new value
		self.value=new

	def GetValue(self):
		retun self.value