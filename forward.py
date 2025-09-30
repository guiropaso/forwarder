from telethon import TelegramClient, events
import requests

# Your credentials
api_id = 21996856
api_hash = '2c74c82b298b170d5c0a286e64b3aaef'
session_name = 'my_session'

# Channels to monitor
source_channels = ['fattyfatclub','unipcsjournal']  # List of channels
# Your n8n webhook URL
n8n_webhook_url = 'https://yallegue.app.n8n.cloud/webhook/355b767f-323b-45e9-8530-b95aff56c784'

client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=source_channels))
async def handler(event):
    message_text = event.message.message
    data = {
        'text': message_text,
        'sender': str(event.message.sender_id),
        'channel': str(event.chat_id)
    }
    # Send to n8n webhook
    try:
        requests.post(n8n_webhook_url, json=data)
    except Exception as e:
        print(f"Error sending to n8n: {e}")

print("Starting client...")
client.start()
client.run_until_disconnected()
