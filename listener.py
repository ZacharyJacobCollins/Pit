import urllib2
import json

def GetMessages():
    messageList = []
    slackHistory = urllib2.urlopen("https://slack.com/api/channels.history?token=xoxb-7542369364-6ZMvoHJWvCnewVYnNCNONBdw&channel=C07RQLZDG&pretty=1").read()
    parsedHistory = json.loads(slackHistory)
    for message in parsedHistory['messages']:
        if len(messageList) < 4:
            messageList.append(message['text'])
        else:
            break  
        
    return messageList