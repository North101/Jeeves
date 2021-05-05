import discord
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(command_prefix='!', description='Jeeves, the A:NR Discord Bot')
extensions = ['cogs.cards']

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)

bot.run(os.environ['DISCORD_TOKEN'])

# GET - https://netrunnerdb.com/api/2.0/public/cards
# GET - https://netrunnerdb.com/api/2.0/public/mwl