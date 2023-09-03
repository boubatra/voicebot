# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC40c0af1e0991461961db8248ad591364'
auth_token = 'db43ece5c71c1599f2423e149ccf9a5e'
client = Client(account_sid, auth_token)

try:
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='+221784673086',
        from_='+18149046606'
    )
    print(call.sid)
except TwilioRestException as e:
    print(e)
