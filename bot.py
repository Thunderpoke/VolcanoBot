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
    "help": "Load a summary of this command!"
}

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
async def _help(ctx, command=""):
    command = command.lower()
    if command == "":
        message = """Hiya there! Guess you need help...
                Do !help [command] for help with a specific command!
                Available commands:
                """

        message += '\n'.join(command_descriptions)

        heading = discord.Embed(title='Help', description=message)
    elif command in command_descriptions:
        heading = discord.Embed(title=command.title(), description=command_descriptions[command])
    else:
        heading = discord.Embed(title="No command found!",
                                description="Sorry, we have not been able to locate that command")

    await ctx.message.add_reaction(emoji='✉')
    await ctx.message.author.send('', embed=heading)

client.run("NjU2MTg1MTc4MDIwMTE4NTUx.XkgjsA.6DdqO1oYLnuztUV6fDpaSM8oJnw")
