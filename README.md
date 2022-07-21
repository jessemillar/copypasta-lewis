# Copypasta Lewis

Copypasta Lewis exists to help your life be more organized. He's sorta like a butler.

## Setup

1. Install the `discord.py` library
	- Install the [SendGrid library](https://github.com/sendgrid/sendgrid-python) if using the Things Cloud functionality
1. Create a Discord bot with "532576331840" permissions and [add it to your server](https://discordjs.guide/preparations/adding-your-bot-to-servers.html#bot-invite-links).
1. Make a `config.json` as outlined below.
1. Manually add `copypasta-lewis` to the two channels you put in `config.json` (in the "edit channel" menu)
1. Run `python3 main.py`.
	- You can specify a specific config file to load by passing it as an argument: `python3 main.py config-custom.json`

### `config.json`

```
{
	"discord_token": "sekret",
	"main_channel_id": 12345,
	"log_channel_id": 67890
}
```

## Usage

> Note: Lewis does **not** care if a message is "pinned." If you want pinned messages to persist, remove any reactions from them prior to enabling Lewis' services.

1. Post messages in your main channel (`main_channel_id`) that you want to use to remind yourself of something later.
1. Once you've done whatever the message reminded you about, add an emoji reaction to the message.
1. Copypasta Lewis will move that message to the log channel (`log_channel_id`) to get it off your plate.
1. Lewis' Discord status will update to show how many more messages you have left to deal with.
