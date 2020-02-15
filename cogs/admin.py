import discord
from discord.ext import commands

command_descriptions = {
            "echo": "The bot says hello, with a very personalised message!",
            "ping": "Find out your latency!",
            "bye": "Say goodbye to the bot!",
            "anger": "Get the bot to be pissed instead of you!",
            "help": "This command!"
        }


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def announce(self, ctx, *, message=""):
        if message == "":
            ctx.channel.purge(limit=1)
            ctx.send("You need to say WHAT to announce!")
            return

        announcement = discord.Embed(
            title="Announcement!",
            description=message,
            colour=discord.Colour.dark_gold()
        )

        await ctx.channel.purge(limit=1)
        await ctx.send("<@&678334943306317862>", embed=announcement)

    @commands.command(name="role")
    async def announcements_role(self, ctx):
        member = ctx.message.author
        role = discord.utils.get(member.guild.roles, name="Announcements")

        if role in member.roles:
            await member.remove_roles(role)
        else:
            await member.add_roles(role)

    @commands.command()
    async def purge(self, ctx, amount=1):
        if ctx.author.id == 525005875098812416:
            await ctx.channel.purge(limit=(amount + 1))


def setup(bot):
    bot.add_cog(Admin(bot))
