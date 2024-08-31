from bot_instance import client  
from events import *
from commands import *
from tokens import bot_token

# runs client with a secret token
client.run(bot_token)