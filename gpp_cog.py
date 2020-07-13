import random
import string

from discord.ext import commands

class GPP(commands.Cog):
    """GPP Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx):
        """Say hi!"""
        await ctx.send(f"Hello {ctx.message.author.name}!")

    @commands.command()
    async def ping(self, ctx):
        """Checks if the bot is on-line"""
        await ctx.send("Pong!")

    @commands.command()
    async def links(self, ctx):
        """Shows a link to a list of our links"""
        await ctx.send("https://gradepointpigeon.cf/")

    @commands.command()
    async def insta(self, ctx):
        """Shows a link to our Instagram"""
        await ctx.send("https://instagram.com/gradepointpigeon")

def setup(bot):
    bot.add_cog(GPP(bot))