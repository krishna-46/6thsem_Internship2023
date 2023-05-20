import os
from twilio.rest import Client
import random

# Your Twilio account SID and auth token
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# The Twilio phone number you want to use for sending SMS
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

# The recipient phone number
recipient_phone_number = 'RECIPIENT_PHONE_NUMBER'

# Generate a random 6-digit OTP
otp = random.randint(100000, 999999)

# Set up the Twilio client
client = Client(account_sid, auth_token)

# Send the OTP via SMS
message = client.messages.create(
    to=recipient_phone_number,
    from_=twilio_phone_number,
    body=f'Your OTP is {otp}')

# Print the message SID
print(f'Message SID: {message.sid}')
