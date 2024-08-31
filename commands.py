from bot_instance import client  # Import the client from the new file

@client.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Brother, Join a voice channel first.")

@client.command(pass_context=True)
async def leave(ctx):
    if ctx.author.voice:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Ma'a salama.")
    else:
        await ctx.send("Im not in a voice chat Subhanallah.")

@client.command()
async def salam(ctx):
    await ctx.send("As-salamu alaykum.")
