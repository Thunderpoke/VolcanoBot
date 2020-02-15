import discord
from discord.ext import commands

command_descriptions = {
        "echo": "The bot says hello, with a very personalised message!",
        "ping": "Find out your latency!",
        "bye": "Say goodbye to the bot!",
        "anger": "Get the bot to be pissed instead of you!",
        "help": "This command!"
        }


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        message = """Hiya there! Guess you need help..."""

        heading = discord.Embed(title='Help', description=message)
        heading.colour = discord.Colour.green()

        for command in command_descriptions:
            heading.add_field(
                name=command,
                value=command_descriptions[command],
                inline=False)

        await ctx.send(embed=heading)


def setup(bot):
    bot.add_cog(Help(bot))
