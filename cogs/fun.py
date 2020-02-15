from discord.ext import commands


class FunCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, message=""):
        if message == "":
            await ctx.send(f'Hello {ctx.author}!')
        else:
            await ctx.send(message)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Latency is: {round(self.bot.latency*1000)}ms')

    @commands.command()
    async def bye(self, ctx):
        await ctx.send("Goodnight")

    @commands.command()
    async def anger(self, ctx):
        await ctx.send("Well that's a f***ing pain in the arse")

    @commands.command()
    async def tryharder(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=t-bgRQfeW64")


def setup(bot):
    bot.add_cog(FunCommands(bot))
