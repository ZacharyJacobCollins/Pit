from sentence import Sentence
from tagger import findSubject
from time import sleep
import listener

def main():
    while True:
        timeStamp = listener.DeleteNotification()
        messages = listener.GetMessages(timeStamp)
<<<<<<< HEAD
=======
from algo import findSubject
from time import sleep
import listener
def main():
    while True:
        messages = listener.GetMessages()
>>>>>>> 5e5baad8e7a5a0f4013c96559b1f56f427def428
        print findSubject(messages)
        if findSubject(messages) != None:
            print "Changing channel"
            listener.UpdateChannelName(findSubject(messages))
<<<<<<< HEAD
            sleep(1)
=======
        sleep(0)
>>>>>>> 5e5baad8e7a5a0f4013c96559b1f56f427def428
if __name__ == '__main__':
    main()


#need to be able to detect subject in question sentences
#subject detection is fucking up
#    delete all messages in CHANNEL  
#while True:
#listener.DeleteChannelMessage(listener.GetMessageTimestamp(0), "C07RQLZDG")
