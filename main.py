from sentence import Sentence
from tagger import findSubject
from time import sleep
import listener

def main():
    while True:
        timeStamp = listener.DeleteNotification()
        messages = listener.GetMessages(timeStamp)
        print findSubject(messages)
        if findSubject(messages) != None:
            print "Changing channel"
            listener.UpdateChannelName(findSubject(messages))
        sleep(0)
if __name__ == '__main__':
    main()


#need to be able to detect subject in question sentences
#subject detection is fucking up
#delete all messages in CHANNEL  
#while True:
#listener.DeleteChannelMessage(listener.GetMessageTimestamp(0))