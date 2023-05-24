import discord
from discord.ext import commands
import json
import os

PREFIX = '.'
CONFIG_FILE = 'bot_config/config.json'

with open(CONFIG_FILE, encoding='utf8') as data:
    config = json.load(data)

bot = commands.Bot(command_prefix=PREFIX, case_insensitive=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))

@bot.command(name = 'ping')
async def ping(ctx):
    print('pong')
    await ctx.send(f"Pong! :ping_pong: `{round(bot.latency * 1000, 2)} ms`")

token = os.environ['DISCORD_BOT_SECRET']

bot.run(token])
        