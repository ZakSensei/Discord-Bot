from bot_instance import client

@client.command()
async def salam(ctx):
    await ctx.send("As-salamu alaykum.")

@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Brother, Join a voice channel first.")

@client.command(pass_context=True)
async def leave(ctx):
    voice_client = ctx.guild.voice_client 
    if voice_client and voice_client.is_connected(): 
        await voice_client.disconnect()  
        await ctx.send("Ma'a salama!")
    else:
        await ctx.send("I'm not in a voice chat, Subhanallah.")