from bot_instance import client  # Import the client from the new file
from events import *
from commands import *
from tokens import *

# runs client with a secret token
client.run(bot_token)