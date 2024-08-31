from bot_instance import client  # Import the client from the new file
from tokens import general_chat_id

@client.event
async def on_member_join(member):
    channel = client.get_channel(general_chat_id)
    await channel.send(f"Alhamdulillah! Welcome to the fold of Islam {member}")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(general_chat_id)
    await channel.send(f"Perhaps {member} was a Kaffir after all. May he be guided.")
