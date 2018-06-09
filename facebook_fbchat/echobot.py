# -*- coding: UTF-8 -*-
from fbchat import log, Client

import fbcredential as fbc

class EchoBot(Client):

    def processmsg(self, message_object):
        print("---------------")
        #print(type(message_object))
        #print(f"msg: {message_object}")
        #print(f"msg: {message_object.text}")

        message_object.text = "New: " + message_object.text
        print("---------------")

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        #log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        self.processmsg(message_object)

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id,
                      thread_type=thread_type)

credentialLine = fbc.FBCredential.getCredential()
email, passwd = fbc.FBCredential.extractCredential(credentialLine)

client = EchoBot(email, passwd)
client.listen()

