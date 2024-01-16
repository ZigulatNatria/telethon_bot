from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 20184483
api_hash = 'ee359dda3d82beb86c80540590edcca2'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))