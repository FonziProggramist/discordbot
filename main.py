import discord
from discord.ext import commands

from config import settings

client = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Я в сети!')

@client.command()
async def test(ctx):
    await ctx.reply('Бот в сети!')

client.run(settings['token'])
