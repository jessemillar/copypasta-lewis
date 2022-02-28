import discord
import json
import logging

logging.basicConfig()
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

    channel = client.get_channel(config["main_channel_id"])
    all_messages = await channel.history(limit = 100000).flatten()

    # Move messages that already have reactions to the log
    i = 0
    while i < len(all_messages):
        print("Processing message {0} of {1}".format(i, len(all_messages)))
        message=all_messages[i]
        if len(message.reactions) > 0:
            await move_message_to_log(message)
        i += 1

async def move_message_to_log(message):
    channel = client.get_channel(config["log_channel_id"])
    message_copy = await channel.send(content = message.content, files = [await f.to_file() for f in message.attachments])

    try:
        await message_copy.add_reaction(message.reactions[0])
    except discord.errors.HTTPException:
        await message_copy.add_reaction("🍑")

    await message.delete()

@client.event
async def on_raw_reaction_add(payload):
    if payload.member == client.user:
        return

    if payload.channel_id != config["main_channel_id"]:
        return

    print("Someone added a reaction!")

    message_original = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    await move_message_to_log(message_original)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.member == client.user:
        return

    if payload.channel_id != config["log_channel_id"]:
        return

    print("Someone removed a reaction!")

    message_original = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    await client.get_channel(config["main_channel_id"]).send(message_original.content)
    await message_original.delete()

# Load config json
with open("config.json") as fp:
    config = json.load(fp)

print("Pooting...")

client.run(config["discord_token"])
