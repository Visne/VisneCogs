import typing

import discord
from redbot.core import commands, bank, Config


class Redistribute(commands.Cog):

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def redistribute(self, ctx: commands.Context, amount: int) -> None:
        """Redistribute an amount of currency to the poorest server members."""
        if amount <= 0:
            await ctx.send("Amount needs to be larger than 0.")
            return

        if not bank.can_spend(ctx.author, amount):
            await ctx.send("You don't have enough " + str(bank.get_currency_name(ctx.guild)) + "!")
            return

        leaderboard: typing.Dict[int, LbData] = dict(await bank.get_leaderboard(None, ctx.guild))
        print(await bank.get_leaderboard(None, ctx.guild))

        if len(leaderboard) == 0:
            await ctx.send("There are no accounts.")
            return
        elif len(leaderboard) == 1:
            await ctx.send("There is noone to redistribute to!")
            return

        while amount > 0:
            a = leaderboard[123]["name"]

        await ctx.send("hello world")


class LbData(typing.TypedDict):
    name: str
    balance: int
    created_at: int
