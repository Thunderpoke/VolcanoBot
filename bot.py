from discord.ext import commands
import hashlib
from urllib.parse import urlencode
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix="$")
client.remove_command("help")

@client.event
async def on_ready():
    print("Bot Is Ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def echo(ctx):
    await ctx.send('Hello!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Latency is:{round(client.latency*1000)}ms')

@client.command()
async def payload(ctx,*,command):
    key = "MyMamaToldMeNeverToAcceptCommandsFromStrangers"
    new_hash = hashlib.sha512((key+command).encode("utf-8")).hexdigest()
    await ctx.send("curl internal.pencilfactoryinvestments.com?"+urlencode({"command":command+":"+new_hash}))

@client.command()
async def bye(ctx):
    await ctx.send("Goodnight")

@client.command()
async def anger(ctx):
    await ctx.send("Well that's a f***ing pain in the arse")

client.load_extension("cogs.help")

client.run("NjcyMTkwMjI4NDY3MDIzODc2.Xkfr_g.I3fSZBTXboGSZmAWjy8Lt2OU4KQ")