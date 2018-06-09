import fbcredential as fbc
from fbchat import Client
from fbchat.models import *

credentialLine = fbc.FBCredential.getCredential()
email, passwd = fbc.FBCredential.extractCredential(credentialLine)

client = Client(email, passwd)

print('Own id: {}'.format(client.uid))

# message to myself
client.send(Message(text='Hi from me!'), thread_id=client.uid,
            thread_type=ThreadType.USER)

# message to other id or group
client.send(Message(text='Hi me!'), thread_id=712934671,
            thread_type=ThreadType.USER)

# `searchForUsers` searches for the user and gives us a list of the results,
# and then we just take the first one, aka. the most likely one:
user = client.searchForUsers('Mark Zuckerberg')[0]

print('user ID: {}'.format(user.uid))
print("user's name: {}".format(user.name))
print("user's photo: {}".format(user.photo))
print("Is user client's friend: {}".format(user.is_friend))

client.logout()

# 100026540660090
