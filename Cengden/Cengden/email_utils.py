# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='ates.toygar@metu.edu.tr',
    to_emails='atestoygar1@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)  
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)