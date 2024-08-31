import discord
from discord.ext import commands
from tokens import *

#client is the bot instance.
#this tells the bot that the '!' means its getting called
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)

#when bot is ready to execute commands it will executre this function
@client.event
async def on_ready():
    print("I am ready to use") 

@client.event
async def on_member_join(member, intents=intents):
    channel = client.get_channel(general_chat_id)
    await channel.send(f"Ah, Welcome to the fold of islam {member} Alhamdulillah!")

@client.command()
async def Salam(ctx):
    await ctx.send("As-salamu alaykum")

#runs client with a secret token
client.run(bot_token)