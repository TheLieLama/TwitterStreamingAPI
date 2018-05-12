from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys

ckey = 'oVG3U04VNOCk5JbRxMUVhuGfK'
csecret = 'wXXQybYOSIXUpoOUk6bVyAI5Pyj61UQeYtuOfCkKwRFo8NfB7b'
atoken = '2877637078-nYbCXZiqCOPaQHua3VM7gFkXQeGxEtaY2bKT95I'
asecret = '98oTh6jrPQt7nIsAOCPoCckq8kEaCCwdPnpXhjarKHe1t'

sys.stdout=open("test.txt","w")

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])

sys.stdout.close()