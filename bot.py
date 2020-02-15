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
    print(f'{member} just joined the server. Why is he allowed here?')


@client.event
async def on_member_remove(member):
    print(f'Well, {member} just left the server. No more Volcano flags for him.')


@client.command()
async def echo(ctx):
    await ctx.send(f'Hello {ctx.author}!')


@client.command()
async def ping(ctx):
    await ctx.send(f'Latency is: {round(client.latency*1000)}ms')


@client.command()
async def bye(ctx):
    await ctx.send("Goodnight")


@client.command()
async def anger(ctx):
    await ctx.send("Well that's a f***ing pain in the arse")


@client.command("help")
async def _help(ctx):
    heading = discord.Embed(title='Help',
        description=
            """Hiya there! Guess you need help...""")

    await ctx.message.add_reaction(emoji='✉')
    await ctx.message.author.send('', embed=heading)

# client.load_extension("cogs.help")

client.run("NjU2MTg1MTc4MDIwMTE4NTUx.XkgZnw.p7bDCiRWnj0LGKyOL3pXrb3mob4")