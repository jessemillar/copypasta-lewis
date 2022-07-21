import sendgrid
import os
import sys
import json
from sendgrid.helpers.mail import *

def get_config_file():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "config.json"

# Load config json
with open(get_config_file()) as fp:
    config = json.load(fp)

sg = sendgrid.SendGridAPIClient(api_key=config["sendgrid_api_key"])
from_email = Email("lewis@compycore.com")
to_email = To(config["things_cloud_email_address")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
