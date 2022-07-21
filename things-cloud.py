import discord
import json
import logging
import sys
import sendgrid
from sendgrid.helpers.mail import *

logging.basicConfig()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Master of your TODO list"))

    channel = client.get_channel(config["main_channel_id"])
    all_messages = await channel.history(limit = 100000).flatten()

    # Move messages that already have reactions to the log
    i = 0
    while i < len(all_messages):
        print("Processing message {0} of {1}".format(i, len(all_messages)))
        message=all_messages[i]
        await process_message(message)
        i += 1

async def process_message(message):
    await send_email(message)
    await move_message_to_log(message)

async def send_email(message):
    sg = sendgrid.SendGridAPIClient(api_key=config["sendgrid_api_key"])
    from_email = Email("lewis@compycore.com")
    to_email = To(config["things_cloud_email_address"])
    subject = message.content
    content = Content("text/plain", "with compliments from Lewis")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    #  print(response.status_code)
    #  print(response.body)
    #  print(response.headers)

async def move_message_to_log(message):
    channel = client.get_channel(config["log_channel_id"])
    message_copy = await channel.send(content = message.content, files = [await f.to_file() for f in message.attachments])

    #  try:
        #  await message_copy.add_reaction(message.reactions[0])
    #  except discord.errors.HTTPException:
        #  await message_copy.add_reaction("🍑")

    await message.delete()

@client.event
async def on_message(message):
    print("Someone typed a message!")
    if message.channel.id != config["main_channel_id"]:
        return
    await process_message(message)

def get_config_file():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "config.json"

# Load config json
with open(get_config_file()) as fp:
    config = json.load(fp)

print("Pooting...")

client.run(config["discord_token"])
