import urllib2
import re
import json
import listener
from time import sleep
from distutils.tests.setuptools_build_ext import if_dl

def GetJson(uri):
    messageText = urllib2.urlopen(uri).read()
    messageJson = json.loads(messageText)
    return messageJson

def GetMessages(timeStampUpdate):
    messageList = []
    messageJson = GetJson("https://slack.com/api/channels.history?token=xoxb-7542369364-6ZMvoHJWvCnewVYnNCNONBdw&channel=C07RQLZDG&pretty=1")
    for i,message in enumerate(messageJson['messages']):
        if len(messageList) < 5:
            messageList.append(message['text'])
        else:
            break
    return messageList

def UpdateChannelName(update):
    urllib2.urlopen("https://slack.com/api/channels.rename?token=xoxp-7542066518-7542253777-7877737223-5f8bd0&channel=C07RQLZDG&name={0}&pretty=1".format(update))
    sleep(1)
    
#Gets the message time stamp by the index of the messages array in the Json file that Slack returns    
def GetMessageTimestamp(index):
    messageJson = GetJson(("https://slack.com/api/channels.history?token=xoxp-7542066518-7542253777-7877737223-5f8bd0&channel=C07RQLZDG&pretty=1"))
    timeStamp = messageJson['messages'][index]['ts']
    return timeStamp
    
def DeleteChannelMessage(timeStamp, channelID):
    urllib2.urlopen("https://slack.com/api/chat.delete?token=xoxp-7542066518-7542253777-7877737223-5f8bd0&ts={0}&channel={1}&pretty=1".format(timeStamp, channelID))

def DeleteNotification():
        pattern = '<@U07FY7FNV|lapso> has renamed the channel from \".*\" to \".*\"'
        messageJson = GetJson("https://slack.com/api/channels.history?token=xoxb-7542369364-6ZMvoHJWvCnewVYnNCNONBdw&channel=C07RQLZDG&pretty=1")
        
        for i,message in enumerate(messageJson['messages']):
            isNotification = bool(re.search(pattern, message['text']))
            if isNotification == True:
                timeStamp = GetMessageTimestamp(i)
                DeleteChannelMessage(timeStamp, "C07RQLZDG")
                return timeStamp
            if i>10:
                break
    