import logging
import os

from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = os.getenv("TOKEN") # Need to specify environment var before running
bot = commands.Bot(command_prefix='p!')

bot.load_extension("gpp_cog")

@bot.event
async def on_ready():
    print(f"{bot.user} is connected to Discord!")

bot.run(TOKEN)
