import twitter
from authorize import authorize

api=authorize()
#print api.VerifyCredentials()

statuses=api.GetUserTimeline("Andillif")

status=statuses[1]
print status.text