# Copypasta Lewis

Copypasta Lewis exists to help your life be more organized. He's sorta like a butler.

## Setup

1. Create a Discord bot and add it to your server.
1. Make a `config.json` as outlined below.
1. Grant `copypasta-lewis` access to the two channels you put in `config.json`
1. Run `python3 main.py`.

### `config.json`

```
{
	"discord_token": "sekret",
	"main_channel_id": 12345,
	"log_channel_id": 67890
}
```

## Usage

1. Post messages in your main channel (`main_channel_id`) that you want to use to remind yourself of something later.
1. Once you've done whatever the message reminded you about, add an emoji reaction to the message.
1. Copypasta Lewis will move that message to the log channel (`log_channel_id`) to get it off your plate.
