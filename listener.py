import urllib2
import json
from time import sleep

def GetMessages():
    messageList = []
    messageText = urllib2.urlopen("https://slack.com/api/channels.history?token=xoxb-7542369364-6ZMvoHJWvCnewVYnNCNONBdw&channel=C07RQLZDG&pretty=1").read()
    messageJson = json.loads(messageText)
    
    for message in messageJson['messages']:
        if len(messageList) < 5:
            messageList.append(message['text'])
        else:
            break  
        
    return messageList
    
def UpdateChannelName(update):
    urllib2.urlopen("https://slack.com/api/channels.rename?token=xoxp-7542066518-7542253777-7877737223-5f8bd0&channel=C07RQLZDG&name={0}&pretty=1".format(update))
    sleep(2)
    messageText = urllib2.urlopen("https://slack.com/api/channels.history?token=xoxp-7542066518-7542253777-7877737223-5f8bd0&channel=C07RQLZDG&pretty=1").read()
    messageJson = json.loads(messageText)
    timeStamp = messageJson['messages'][0]['ts']
    #urllib2.urlopen("https://slack.com/api/chat.delete?token=xoxp-7542066518-7542253777-7877737223-5f8bd0&ts={0}&channel=C07RQLZDG&pretty=1".format(timeStamp))