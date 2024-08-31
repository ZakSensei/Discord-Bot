import discord
from discord.ext import commands
from tokens import *

#client is the bot instance.
#this tells the bot that the '!' means its getting called
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!', intents=intents)
channel = client.get_channel(general_chat_id)

#when bot is ready to execute commands it will executre this function
@client.event
async def on_ready():
    print("I am ready to use") 

@client.event
async def on_member_join(member, intents=intents):
    channel = client.get_channel(general_chat_id)
    await channel.send(f"Alhamdulillah! Welcome to the fold of islam {member}")

@client.event
async def on_member_remove(member, intents=intents):
    await channel.send(f"Perhaps {member} was a Kaffir after all. May he be guided.")

#author is the user running the command
#if author running command is in a voice channel it gets the channel id and connects to it
@client.command(pass_context= True)
async def join(ctx):
    if (ctx.author.voice):  
            channel = ctx.message.author.voice.channel
            await channel.connect()
    else:
         await ctx.send("Brother, Join a voice channel first.")

#if bot is in a voice channel it will leave
#voice_client = voice channel
@client.command(pass_context= True)
async def leave(ctx):
    if (ctx.author.voice):  
            await ctx.guild.voice_client.disconnect()
            await ctx.send("Ma'a salama.")
    else:
         await ctx.send("Im not in a voice chat Subhanallah.")

@client.command()
async def salam(ctx):
    await ctx.send("As-salamu alaykum.")

#runs client with a secret token
client.run(bot_token)