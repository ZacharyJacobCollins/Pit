from sentence import Sentence
from algo import findSubject
from time import sleep
import listener
def main():
    while True:
        messages = listener.GetMessages()
        print findSubject(messages)
        if findSubject(messages) != None:
            print "Changing channel"
            listener.UpdateChannelName(findSubject(messages))
        sleep(2)
if __name__ == '__main__':
    main()
