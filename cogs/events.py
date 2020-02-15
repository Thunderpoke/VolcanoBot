from discord.ext import commands

class MainEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Is Ready")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.bot.get_channel(658064237112983554).send(
            f'{member} just joined the server. Why is he allowed here?')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.bot.get_channel(658064237112983554).send(
            f"""Well, {member} just left the server.
             No more Volcano flags for him.""")

def setup(bot):
    bot.add_cog(MainEvents(bot))
