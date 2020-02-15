import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix="$")
client.remove_command("help")


client.load_extension("cogs.fun")
client.load_extension("cogs.events")
client.load_extension("cogs.help")


@client.command()
async def purge(ctx, amount=1):
    if ctx.author.id == 525005875098812416:
        await ctx.channel.purge(limit=(amount + 1))

client.run("")
