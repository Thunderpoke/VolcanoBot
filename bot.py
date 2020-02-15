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

command_descriptions = {
    "echo": "The bot says hello, with a very personalised message!",
    "ping": "Find out your latency!",
    "bye": "Say goodbye to the bot!",
    "anger": "Get the bot to be pissed instead of you!",
    "help": "This command!"
}

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


@client.command("help")
async def _help(ctx):
    message = """Hiya there! Guess you need help..."""

    heading = discord.Embed(title='Help', description=message)
    heading.colour = discord.Colour.green()

    for command in command_descriptions:
        heading.add_field(name=command, value=command_descriptions[command], inline=False)

    await ctx.send(embed=heading)

@client.command()
async def purge(ctx, amount=1):
    if ctx.author.id == 525005875098812416:
        await ctx.channel.purge(limit=(amount + 1))

client.run("NjU2MTg1MTc4MDIwMTE4NTUx.XkgxDw.fDBVFHWNfLU7x2rZgxURC5lf1UM")
