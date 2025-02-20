# users/utils.py
from twilio.rest import Client

def send_otp(phone_number, otp):
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is {otp}",
        from_='',  # Your Twilio phone number
        to=str(phone_number)
    )
    print(f"Message SID: {message.sid}")