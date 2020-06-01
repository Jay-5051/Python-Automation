from twilio.rest import Client

account_sid = 'AC6f8a69b09dd60cfc2b5debae038c0d92'
auth_token = '821baef36ff5ecf894e18bb7bacdd51d'
client = Client(account_sid, auth_token)

def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello',
        to='whatsapp:+918182828582'
    )

    print(message.sid)