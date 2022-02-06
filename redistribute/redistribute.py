from redbot.core import commands
from redbot.core import bank


class Redistribute(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def redistribute(self, ctx: commands.Context, amount: int):


        await ctx.send("hello world")
