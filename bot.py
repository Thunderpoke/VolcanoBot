import discord.utils
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log',
    encoding='utf-8',
    mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="$")
bot.remove_command("help")

bot.load_extension("cogs.fun")
bot.load_extension("cogs.events")
bot.load_extension("cogs.help")
bot.load_extension("cogs.admin")

bot.run("NjU2MTg1MTc4MDIwMTE4NTUx.XkhZBQ.N2Y90GoT-lzAx0h_C5DYkGse9Sk")
