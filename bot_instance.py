import discord
from discord.ext import commands

# Creating the bot instance here
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
