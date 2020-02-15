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



@client.event
async def on_ready():
    print("Bot Is Ready")


@client.event
async def on_member_join(member):
    client.get_channel(658064237112983554).send(f'{member} just joined the server. Why is he allowed here?')


@client.event
async def on_member_remove(member):
    client.get_channel(658064237112983554).send(f'Well, {member} just left the server. No more Volcano flags for him.')


@client.command()
async def echo(ctx, *, message):
    if message == "":
        await ctx.send(f'Hello {ctx.author}!')
    else:
        await ctx.send(message)


@client.command()
async def ping(ctx):
    await ctx.send(f'Latency is: {round(client.latency*1000)}ms')


@client.command()
async def bye(ctx):
    await ctx.send("Goodnight")


@client.command()
async def anger(ctx):
    await ctx.send("Well that's a f***ing pain in the arse")


client.load_extension("cogs.help")

@client.command()
async def purge(ctx, amount=1):
    if ctx.author.id == 525005875098812416:
        await ctx.channel.purge(limit=(amount + 1))

client.run("NjcyMTkwMjI4NDY3MDIzODc2.Xkg3Vw.OA28IE7WigmtocvTEadXYgME7gM")
