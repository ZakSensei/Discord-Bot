import discord
from discord.ext import commands
from tokens import bot_token

#client is the bot instance.
#this tells the bot that the '!' means its getting called
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)

#when bot is ready to execute commands it will executre this function
@client.event
async def on_ready():
    print("I am ready to use") 

#when usere says 
@client.command()
async def akhi(ctx):
    await ctx.send("As-salamu alaykum")

#runs client with a secret token
client.run(bot_token)