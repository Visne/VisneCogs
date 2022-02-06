from .redistribute import Redistribute


def setup(bot):
    bot.add_cog(Redistribute(bot))
